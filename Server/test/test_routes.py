import json
from app import app
import pytest
import jwt
from datetime import datetime, timedelta

client = app.test_client()

def test_BasePath_GivenAGETRequest_ShouldReturnTheStringHelloWorld():
    #Prepare data
    url = '/'

    #Act
    res = client.get(url)

    #Assert
    assert res.get_data() == b'Hello World!'
    assert res.status_code == 200

# @pytest.mark.xfail(reason="Still need to cater for the user tokens")
def test_PicturePath_GivenAnUploadedImage_ShouldReturnAnImageByteArray():
    #Prepare Data
    url = '/picture'
    key = "secret"
    accessToken = jwt.encode({'email' :'admin@test.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
    header = {
        'Authorization': 'Bearer {}'.format(accessToken)
    }

    #Act
    res = client.post(url, headers=header,content_type="application/json", data=json.dumps({'picture': 'Server/images/image1.jpg'}))

    #Assert
    assert res.status_code == 200
    assert res.content_type == "application/json"

# @pytest.mark.xfail(reason="Fix the database config for register")
def test_RegisterPath_GivenUserCredentials_ShouldReturnABooleanValue():
    #Prepare Data
    user = {
        'name': 'Neo',
        'surname': 'Seefane',
        'email': 'neoseefane13@gmail.com',
        'password': '1234@Neo'
    }
    url = '/register'

    #Act
    res = client.post(url, data=json.dumps(user))
    
    #Assert
    assert res.status_code == 200

# @pytest.mark.xfail(reason="Fix the database config for login")
def test_LoginPath_GivenUserLoginCredentials_ShouldReturnTheStringFailOrSuccess():
    #Prepare Date
    invalid_user = {
        'username': 'neoseefane13@gmail.com',
        'password': '1234@Neo'
    }
    url = '/login'

    #Act
    res = client.post(url, data=json.dumps(invalid_user))

    #Assert
    assert res.status_code == 200
    

def test_TemplatePath_GivenAGETRequest_ShouldReturnTheindexHtmlPage():
    #Prepare Data
    url = '/template'

    #Act
    res = client.get(url)

    #Assert
    assert res.status_code == 200
