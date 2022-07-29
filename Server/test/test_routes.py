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

# app.config.from_object('config_default.TestingConfig')
db = User()
client = app.test_client()

# def test_BasePath_GivenAGETRequest_ShouldReturnTheStringHelloWorld():
#     #Prepare data
#     url = '/'

#     #Act
#     res = client.get(url)

#     #Assert 
#     assert res.get_data() == b'Hello World!'
#     assert res.status_code == 200
##Fix
# @pytest.mark.xfail(reason="Still need to cater for the user tokens")
def test_PicturePath_GivenAnUploadedImage_ShouldReturnAnImageByteArray():
    #Prepare Data
    url = '/picture'
    key = "secret"
    accessToken = jwt.encode({'email' :'hardcode810@gmail.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
    header = {
        'x-access-token':accessToken
    }
    with open("../images/image1.jpg", "rb") as img_file:
                b64picture = base64.b64encode(img_file.read())
    #Act
    res = client.post(url, headers=header,content_type="application/json", data=json.dumps({'picture': str('data:image/png;base64,'+str(b64picture))}))

    #Assert
    assert res.status_code == 200
    # assert res.content_type == "application/json"


def test_RegisterPath_GivenUserCredentials_ShouldReturnABooleanValue():
    #Prepare Data
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    name= "name "+current_time
    surname= "surname "+current_time
    email= "email "+current_time
    password= "password "+current_time
    code = str(random.randint(1000, 9999))
    if(db!=None):
        db.insert_code(email, code)
    user = {
        'name': name,
        'surname': surname,
        'email': email,
        'password': password,
        'code': code
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

def test_UploadUserHistory_GivenAGETRequest_ShouldReturnStatusCode200():
    # with app.app_context():
    #Prepare Data
    url = '/uploadhistory'
    key = "secret"
    # accessToken = create_access_token('test-user-upload')
    accessToken = jwt.encode({'email' :'hardcode810@gmail.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
    header = {
    'x-access-token':accessToken
    }

    #Act
    res = client.get(url, headers=header, content_type="application/json")

    #Assert
    assert res.status_code == 200


def test_UserFeedback_GivenUserFeedback_ShouldReturnSuccess():
    # with app.app_context():
    #Prepare Data
    url = '/feedback'
    key = "secret"
    # accessToken = create_access_token('test-user-upload')
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

def test_UserFeedback_GivenUserFeedback_ShouldReturnSuccess():
    # with app.app_context():
    #Prepare Data
    url = '/feedback'
    key = "secret"
    # accessToken = create_access_token('test-user-upload')
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

def test_ResetPasswordPath_GivenExistingUserLoginCredentials_ShouldReturnTheStatusCode200():
    #Prepare Date
    url = '/resetpassword'
    key = "secret"
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

    request ={
        'email': email,
        'password': password
    }

    #Act
    res = client.post(url,content_type="application/json",data=json.dumps(request))

    print(res.response)
    #Assert
    assert res.status_code == 200

    
def test_SendEmailPath_GivenANewEmail_ShouldReturnTheStatusCode200():
    #Prepare Date
    url = '/sendEmail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    email= "email "+current_time
    #Act

    request ={
        'email': email
    }

    #Act
    res = client.post(url,content_type="application/json",data=json.dumps(request))

    print(res.response)
    #Assert
    assert res.status_code == 200
    # assert res.response == 'success'
    
def test_ResetPasswordCodePath_GivenANewCode_ShouldReturnTheStatusCode200():
    #Prepare Date
    url = '/resetpasswordcode'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    email= "email "+current_time
    code = str(random.randint(1000, 9999))
    
    #Act
    if(db!=None):
        db.insert_code(email, code)
    request ={
        'email': email,
        'code': code
    }

    res = client.post(url,content_type="application/json",data=json.dumps(request))
    print(res.response)
    #Assert
    assert res.status_code == 200
    
def test_ResetPasswordEmailPath_GivenExistingUser_ShouldReturnTheStatusCode200():
    #Prepare Date
    url = '/resetpasswordemail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    name= "name "+current_time
    surname= "surname "+current_time
    email= "email"+current_time+"@gmail.com"
    password= "password "+current_time
    #Act
    db = User()
    if(db != None):
        result = db.register(name, surname, email, password)

    request ={
        'email': email
    }

    #Act
    res = client.post(url,content_type="application/json",data=json.dumps(request))

    print(res.response)
    #Assert
    assert res.status_code == 200

def test_PlotGraphPath_GivenUserFeedback_ShouldReturnSuccess():
    # with app.app_context():
    #Prepare Data
    url = '/plotting'
    key = "secret"
    # accessToken = create_access_token('test-user-upload')
    accessToken = jwt.encode({'email' :'hardcode810@gmail.com', 'exp' : datetime.utcnow() + timedelta(minutes=60)}, key,algorithm="HS256")
    header = {
    'x-access-token':accessToken
    }
    request ={
        'formula': "2*x"
    }
    #Act
    res = client.post(url, headers=header, content_type="application/json",data=json.dumps(request))

    #Assert
    assert res.status_code == 200