import os
from database.mockDatabase import mockDatabase
from datetime import datetime
dirname = os.path.dirname(__file__)

def test_InsertFeedback_GivenNewUserFeedback_ShouldReturnTrue():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        name= "name "+current_time
        surname= "surname "+current_time
        email= "email "+current_time
        password= "password "+current_time
        feedback = "feedback "+current_time
        
        db = mockDatabase()
        if(db != None):
            db.register(name, surname, email, password)
            person = db.getUserWithEmail(email)

            #Act
            result = db.insert_feedback(person[0],feedback)
            #Assert
            assert result == True
        else:
            assert False
    except Exception as e:
        print(f"Test Error : {e}")
        assert False