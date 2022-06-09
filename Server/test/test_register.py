import os
from database.database import User
from datetime import datetime
dirname = os.path.dirname(__file__)

def test_RegisterUser_GivenANewUser_ShouldReturnTrue():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        name= "name "+current_time
        surname= "surname "+current_time
        email= "email "+current_time
        password= "password "+current_time
        #Act
        db = User()
        if(db != None):
            result = db.register(name, surname, email, password)
            
            #Assert
            assert result == True
        else:
            assert False
    except Exception as e:
        print(f"Test Error : {e}")
        assert False