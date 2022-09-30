import os
from database.mockDatabase import mockDatabase
from datetime import datetime
dirname = os.path.dirname(__file__)

def test_GetCode_GivenAnExistingCode_ShouldReturnTheCode():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        email= "email "+current_time
        code= "code "+current_time

        db = mockDatabase()
        if(db != None):
            db.insertCode(email, code)

            #Act
            result = db.getCode(email)
            print(result)
            #Aseert
            assert result[1] == email
            assert result[2] == code
        else:
            assert False

    except Exception as e:
        print(f"Test Error : {e}")
        assert False

def test_GetCode_GivenANonExistingCode_ShouldReturnNone():
    #Prepare
    try :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        email= "email "+current_time

        db = mockDatabase()
        if(db != None):

            #Act
            result = db.getCode(email)
            #Aseert
            assert result == None
        else:
            assert False

    except Exception as e:
        print(f"Test Error : {e}")
        assert False


