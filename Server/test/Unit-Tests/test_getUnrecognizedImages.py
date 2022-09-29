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
    except Exception as e:
        print(f"Test Error : {e}")
        assert False