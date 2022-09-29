import os
from database.mockDatabase import mockDatabase
from datetime import datetime
dirname = os.path.dirname(__file__)

def test_UpdatePassword_GivenAnExistingUserAndNewPassword_ShouldReturnTrue():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        name= "name "+current_time
        surname= "surname "+current_time
        email= "email "+current_time
        password= "password "+current_time
        newPassword = "newPassword "+current_time
        db = mockDatabase()
        if(db != None):
            db.register(name, surname, email, password)

            #Act
            result = db.updatePassword(email, newPassword)

            #Assert
            assert result == True
        else:
            assert False
        
        
    except Exception as e:
        print(f"Test Error : {e}")
        assert False

def test_UpdatePassword_GivenANonExistingUser_ShouldReturnFalse():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        email= "email "+current_time
        newPassword= "newPassword "+current_time

        db = mockDatabase()
        if(db != None):

            #Act
            result = db.updatePassword(email, newPassword)

            #Assert
            assert result == False
        else:
            assert False
        
        
    except Exception as e:
        print(f"Test Error : {e}")
        assert False