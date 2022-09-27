import json
from os import access
import random
import re
from app import app
import pytest
import base64
import jwt
from database.database import User
from datetime import datetime, timedelta
# from flask_jwt_extended import create_access_token

app.config.from_object('config_default.TestingConfig')
db = app.config['DATABASE']
client = app.test_client()


# @pytest.mark.xfail(reason="Still need to cater for the user tokens")
# def test_PicturePath_GivenAnUploadedImage_ShouldReturnAnImageByteArray():
#     #Prepare Data
#     url = '/picture'
#     key = "secret"
#     accessToken = jwt.encode({'email' :'hardcode810@gmail.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
#     header = {
#         'x-access-token':accessToken
#     }
#     with open("../images/download.png", "rb") as img_file:
#                 b64picture = base64.b64encode(img_file.read())
#     # print(b64picture[b64picture.find("b'")+1:])
#     b64picture=str(b64picture)
#     # print(b64picture[b64picture.find("b'")+2:])
#     #Act
#     res = client.post(url, headers=header,content_type="application/json", data=json.dumps({'picture': 'data:image/png;base64,'+b64picture[b64picture.find("b'")+2:]}))

#     #Assert
#     assert res.status_code == 200
#     # assert res.content_type == "application/json"


def test_RegisterPath_GivenUserCredentials_ShouldReturnStatusCode200():
    #Prepare Data
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    name= "name "+current_time
    surname= "surname "+current_time
    email= "email "+current_time
    password= "password "+current_time
    code = str(random.randint(1000, 9999))
    db.insert_code(email, code)
    user = {
        'name': name,
        'surname': surname,
        'email': email,
        'password': password,
        'code':code
    }
    url = '/register'

    #Act
    res = client.post(url, content_type="application/json",data=json.dumps(user))
    
    #Assert
    assert res.status_code == 200

def test_LoginPath_GivenUserLoginCredentials_ShouldReturnStatusCode200():
    #Prepare Date
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    name= "name "+current_time
    surname= "surname "+current_time
    email= "email "+current_time
    password= "password "+current_time
    #Act
    # db = User()
    if(db != None):
        result = db.register(name, surname, email, password)

    valid_user = {
        'email': email,
        'password': password
    }
    url = '/login'

    #Act
    res = client.post(url, content_type="application/json",data=json.dumps(valid_user))

    #Assert
    assert res.status_code == 200
    

def test_UploadUserHistory_GivenAGETRequest_ShouldReturnStatusCode200():
    #Prepare Data
    url = '/uploadhistory'
    key = "secret"

    accessToken = jwt.encode({'email' :'hardcode810@gmail.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
    header = {
    'x-access-token':accessToken
    }

    #Act
    res = client.get(url, headers=header, content_type="application/json")

    #Assert
    assert res.status_code == 200


def test_UserFeedback_GivenUserFeedback_ShouldReturnStatusCode200():
    #Prepare Data
    url = '/feedback'
    key = "secret"

    accessToken = jwt.encode({'email' :'hardcode810@gmail.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
    header = {
    'x-access-token':accessToken
    }
    request ={
        'feedback': "test feedback"
    }
    #Act
    res = client.post(url, headers=header, content_type="application/json",data=json.dumps(request))

    #Assert
    assert res.status_code == 200

def test_Activities_GivenAGETRequest_ShouldReturnStatusCode200():
    #Prepare Data
    url = '/activities'
    key = "secret"

    accessToken = jwt.encode({'email' :'hardcode810@gmail.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
    header = {
    'x-access-token':accessToken
    }

    #Act
    res = client.get(url, headers=header, content_type="application/json")

    #Assert
    assert res.status_code == 200

def test_IncrementActivity_GivenTheTypeOfActivity_ShouldReturnStatusCode200():
    #Prepare Data
    url = '/incrementActivity'
    key = "secret"

    accessToken = jwt.encode({'email' :'hardcode810@gmail.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
    header = {
    'x-access-token':accessToken
    }
    request ={
        'activity': "downloads"
    }
    #Act
    res = client.post(url, headers=header, content_type="application/json",data=json.dumps(request))

    #Assert
    assert res.status_code == 200