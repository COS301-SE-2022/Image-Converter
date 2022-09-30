import os
from database.mockDatabase import mockDatabase
from datetime import datetime
dirname = os.path.dirname(__file__)

def test_GetUnrecognizedImages_GivenAnExistingHistoryRecod_ShouldReturnTrue():
    #Prepare
    try:
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
            result = db.insert_image(arr,arr2,person[0])
            #Act
            result = db.getUnrecognizedImages()
            #Assert
            assert result != []
        else:
            assert False
    except Exception as e:
        print(f"Test Error : {e}")
        assert False