import os
import bcrypt
from database.mockDatabase import User
from datetime import datetime
dirname = os.path.dirname(__file__)

def test_GetUserByEmail_GivenAnExistingUser_ShouldReturnTheUser():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        name= "name "+current_time
        surname= "surname "+current_time
        email= "email "+current_time
        password= "password "+current_time

        db = User()
        if(db != None):
            db.register(name, surname, email, password)

            #Act
            result = db.getUserWithEmail(email)
            print(result)
            #Aseert
            assert result[1] == name
            assert result[2] == surname
            assert bcrypt.checkpw(password.encode('UTF-8'), result[3].encode('UTF-8'))
            assert result[4] == email

        else:
            assert False
        
        
    except Exception as e:
        print(f"Test Error : {e}")
        assert False
