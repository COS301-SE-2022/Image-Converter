import os
from database.mockDatabase import mockDatabase
from datetime import datetime
dirname = os.path.dirname(__file__)

def test_UpdateGraphType_GivenAnExistingHistoryRecod_ShouldReturnTrue():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        name= "name "+current_time
        surname= "surname "+current_time
        email= "email "+current_time
        password= "password "+current_time
        newGraphType = "newGraphType "+current_time
        db = mockDatabase()
        if(db != None):
            db.register(name, surname, email, password)
            person = db.getUserWithEmail(email)
            arr = bytearray(name, 'utf-8')
            arr2 = bytearray(surname, 'utf-8')
            db.insert_image(arr,arr2,person[0])

            #Act
            result = db.updateGraphType(newGraphType,db.db_history_id-1)

            #Assert
            assert result == True
        else:
            assert False
        
    except Exception as e:
        print(f"Test Error : {e}")
        assert False

def test_UpdateGraphType_GivenANonExistingHistoryRecod_ShouldReturnFalse():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        newGraphType = "newGraphType "+current_time
        db = mockDatabase()
        if(db != None):

            #Act
            result = db.updateGraphType(newGraphType,0)

            #Assert
            assert result == False
        else:
            assert False
        
        
    except Exception as e:
        print(f"Test Error : {e}")
        assert False