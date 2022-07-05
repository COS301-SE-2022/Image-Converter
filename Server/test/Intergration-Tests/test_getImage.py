import os
from database.mockDatabase import mockDatabase
from datetime import datetime
dirname = os.path.dirname(__file__)

def test_GetImage_GivenExistingImages_ShouldReturnHistoryRecord():
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
            person = db.getUserWithEmail(email)
            arr = bytearray(name, 'utf-8')
            arr2 = bytearray(surname, 'utf-8')
            db.insert_image(arr,arr2,person[0])

            #Act
            result = db.get_image(person[0])

            #Assert
            assert bytes(result[3]) == arr
            assert bytes(result[4]) == arr2
        else:
            assert False
    except Exception as e:
        print(f"Test Error : {e}")
        assert False

def test_GetImage_GivenExistingImagesAndAUserThatDoesnotExist_ShouldReturnHistoryRecord():
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
            person = db.getUserWithEmail(email)
            arr = bytearray(name, 'utf-8')
            arr2 = bytearray(surname, 'utf-8')
            db.insert_image(arr,arr2,person[0])

            #Act
            result = db.get_image(person[0]+db.db_id+10)

            #Assert
            assert result == None
        else:
            assert False
    except Exception as e:
        print(f"Test Error : {e}")
        assert False

