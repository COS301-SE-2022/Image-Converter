import os
from database.mockDatabase import mockDatabase
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
        db = mockDatabase()
        if(db != None):
            result = db.register(name, surname, email, password)
            
            #Assert
            assert result == True
        else:
            assert False
    except Exception as e:
        print(f"Test Error : {e}")
        assert False

def test_RegisterUser_GivenAnExistingUser_ShouldReturnFalse():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        name= "name "+current_time
        surname= "surname "+current_time
        email= "email "+current_time
        password= "password "+current_time
        #Act
        db = mockDatabase()
        if(db != None):
            db.register(name, surname, email, password)
            result = db.register(name, surname, email, password)
            
            #Assert
            assert result == False
        else:
            assert False
    except Exception as e:
        print(f"Test Error : {e}")
        assert False

def test_RegisterUser_GivenAnExistingEmail_ShouldReturnFalse():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        name= "name "+current_time
        surname= "surname "+current_time
        email= "email "+current_time
        password= "password "+current_time
        #Act
        db = mockDatabase()
        if(db != None):
            db.register(name, surname, email, password)
            result = db.register(name+"2", surname+"2", email, password+"2")
            
            #Assert
            assert result == False
        else:
            assert False
    except Exception as e:
        print(f"Test Error : {e}")
        assert False

