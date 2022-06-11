import json
from os import access
from app import app
import pytest
import base64
import jwt
from database.database import User
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token

app.config.from_object('config_default.TestingConfig')
db = app.config['DATABASE']
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
    accessToken = jwt.encode({'email' :'hardcode810@gmail.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
    header = {
        'x-access-token':accessToken
    }
    with open("images/image1.jpg", "rb") as img_file:
                b64picture = base64.b64encode(img_file.read())
    #Act
    res = client.post(url, headers=header,content_type="application/json", data=json.dumps({'picture': str('data:image/png;base64,'+str(b64picture))}))

    #Assert
    assert res.status_code == 200
    assert res.content_type == "application/json"

# @pytest.mark.xfail(reason="Fix the database config for register")
def test_RegisterPath_GivenUserCredentials_ShouldReturnABooleanValue():
    #Prepare Data
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    name= "name "+current_time
    surname= "surname "+current_time
    email= "email "+current_time
    password= "password "+current_time
    user = {
        'name': name,
        'surname': surname,
        'email': email,
        'password': password
    }
    url = '/register'

    #Act
    res = client.post(url, content_type="application/json",data=json.dumps(user))
    
    #Assert
    assert res.status_code == 200

# @pytest.mark.xfail(reason="Fix the database config for login")
def test_LoginPath_GivenUserLoginCredentials_ShouldReturnTheStringFailOrSuccess():
    #Prepare Date
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

    invalid_user = {
        'email': email,
        'password': password
    }
    url = '/login'

    #Act
    res = client.post(url, content_type="application/json",data=json.dumps(invalid_user))

    #Assert
    assert res.status_code == 200
    

def test_TemplatePath_GivenAGETRequest_ShouldReturnTheindexHtmlPage():
    #Prepare Data
    url = '/template'

    #Act
    res = client.get(url)

    #Assert
    assert res.status_code == 200

def test_UploadUserHistory_GivenAGETRequest_ShouldReturn():
    with app.app_context():
        #Prepare Data
        url = '/uploadhistory'
        accessToken = create_access_token('test-user-upload')
        header = {
            'Authorization': 'Bearer {}'.format(accessToken)
        }

        #Act
        res = client.post(url, headers=header)

        #Assert
        assert res.status_code == 200