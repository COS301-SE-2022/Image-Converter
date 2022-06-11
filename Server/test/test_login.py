import os
from database.mockDatabase import mockDatabase
from datetime import datetime
dirname = os.path.dirname(__file__)

def test_LoginUser_GivenAnExistingUser_ShouldReturnTrue():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        name= "name "+current_time
        surname= "surname "+current_time
        email= "email "+current_time
        password= "password "+current_time

        db = mockDatabase()
        if(db != None):
            db.register(name, surname, email, password)

            #Act
            result = db.login(email, password)

            #Assert
            assert result == True
        else:
            assert False
        
        
    except Exception as e:
        print(f"Test Error : {e}")
        assert False
