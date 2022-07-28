import datetime
from functools import wraps
from lib2to3.pytree import Node
from attr import s
import jwt
from flask import Flask, json, jsonify, render_template, request, session
from converter.smoothing import smoothing
from converter.templateMatching import Matching
from converter.image_classification import Classification
from database.database import User
from database.sendEmail import Email
from converter.ConvertFomat import ConvertFomat
from converter.watermark import AddMark
from flask import Response
from flask_cors import CORS
import base64
import cv2
import os
import random
import io
import PIL.Image as Image
import numpy as np




app = Flask(__name__)
app.secret_key = "super secret key"
CORS(app)

def token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = None
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            print(token)
            return jsonify({'result': 'Token is not found or invalid!'}), 401

        try:
            db = User()
            data = jwt.decode(token, 'secret', "HS256")
            user = db.getUserWithEmail(data['email'])
        except Exception as e:
            return jsonify({'result': str(e)}), 401
        return f(user, *args, **kwargs)

    return decorated


@app.route('/')
def index():
    return "Hello World!"


@app.route('/test', methods=['POST'])
@token
def test(user):
    username = str(request.json['email'])
    print(user)
    return jsonify({'result': username})



@app.route('/picture', methods=['POST'])
@token
def upload_image(user):
    db=User()
    if(db!=None):
        picture = request.json['picture']
        # print(picture)
        if picture is not None:
            print("picture is not None")
            base64_picture=base64.b64encode((bytes(picture[picture.find(",")+1:].encode('utf-8'))))
            imageReturned = "data:image/png;base64,"
            imgdata = base64.b64decode(str(picture[picture.find(",")+1:]))
            img = Image.open(io.BytesIO(imgdata))
            opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
            
            image_uploaded = bytearray(base64_picture)
            img_class = Classification(picture)
            # print(type(opencv_img))
            # templateMatch = Matching(opencv_img)
            #-------> img_class = Classification(opencv_img)
            # print(templateMatch.graphType)
            # print(templateMatch.perfectMatch)
            print("#########################################")
            print(img_class.graphType)
            print("#########################################")

            imageCleaner = smoothing(opencv_img)

            imageResult =imageCleaner.clean_noise()


            # addLogo = AddMark(opencv_img)
            # addLogo.Dev

            with open("images/original/Graph.png", "rb") as img_file:
                b64picture = base64.b64encode(img_file.read())
            # print("b64picture")
            image_converted = bytearray(b64picture)
            
            if(db.insert_image(opencv_img, imageResult, user[0])):
                print("Image inserted")
            db_image = db.get_image(user[0])
            
            graphType = "This graph is"
            if(templateMatch.perfectMatch>5):
                graphType = graphType + " a "+templateMatch.graphType
            else:
                graphType= graphType + " not recognized by the system"

            conv=ConvertFomat()
            conv.covertImgFormat(db_image[4])
        return jsonify({'image': db_image[4], 'png':conv.getPng(),'jpg':conv.getJpg(), 'graphType': graphType})

    else:
        return {'response': 'failed'}, 400


@app.route('/login', methods=['POST'])
def auth_login():
    db = User()
    if(db != None):
        username = str(request.json['email'])
        password = str(request.json['password'])
        print(db.getUserWithEmail(username)[0])
        if(db.login(username,password)):
            token = jwt.encode({'email': username, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(hours=2)}, 'secret', algorithm="HS256")
            result = "success"
            return jsonify({'result': result, 'token': str(token)})
        else:
            return jsonify({'result': 'failed'})
    else:
        return {'response': 'failed'}, 400


@app.route('/register', methods=["POST"])
def register():
    db = User()
    if(db != None):
        name = str(request.json["name"])
        surname = str(request.json["surname"])
        email = str(request.json["email"])
        password = str(request.json["password"])
        code = str(request.json["code"])
        print(code)
        if db.get_code(email)[2]==code:
            if(db.register(name, surname, email, password)):
                token = jwt.encode({'email': email, 'exp': datetime.datetime.utcnow(
                ) + datetime.timedelta(hours=2)}, 'secret', algorithm="HS256")
                
                result = "success"
                return jsonify({'result': result, 'token': str(token)})
            else:
                return {'response': 'failed'}, 400
        else:
            return {'response': 'failed'}, 400
    else:
            return {'response': 'failed'}, 400

@app.route('/template')
def img():
    return render_template('index.html', images = True)

@app.route('/uploadhistory', methods=["GET"])
@token
def uploadhistory(user):
    
    db = User()
    if(db != None):
        imageReturned = "data:image/png;base64,"
        db_image_array=db.get_image_history(user[0])
        OriginalImagelist=[]
        IndexArray=[]
        proccesedImagelist=[]
        for x in db_image_array:
            IndexArray.append(x[0])
            OriginalImagelist.append(x[3]) 
            proccesedImagelist.append(x[4]) 


        return jsonify({"OriginalImage": OriginalImagelist,"proccesedImage": proccesedImagelist ,"Index":IndexArray})
    else:
        return {'response': 'failed'}, 400

@app.route('/deletehistory' ,methods =['POST'])
@token
def delete_user_history(user):
    #check the environment 
    db=User()
    if(db!=None):
        index = request.json['index']
        print(index)
        if index is not None:
            if db.delete_history(index) is True:
                print("Image deleted")
                return jsonify({'response': 'success'})
            else:
                return jsonify({'response': 'failed'})
        else:
            return {'response': 'failed'}, 400
    else:
        return {'response': 'failed'}, 400


@app.route('/feedback' ,methods =['POST'])
@token
def user_feedback(user):
    db=User()
    if(db!=None):
        feedback = request.json['feedback']
        if feedback is not None:
            if db.insert_feedback(user[0],feedback) is True:
                print("feedback inserted")
                return jsonify({'response': 'success'})
            else:
                return jsonify({'response': 'failed'})
        else:
            return {'response': 'failed'}, 400
    else:
        return {'response': 'failed'}, 400

@app.route('/resetpassword', methods=["POST"])
def reset_password():
    db = User()
    if(db != None):
        email = str(request.json['email'])
        newPassword = str(request.json['password'])
        if(db.updatePassword(email, newPassword)):
            return {'response': 'success'}, 200
        else:
            return {'response': 'failed'}, 400
    else:
        return {'response': 'failed'}, 400


@app.route('/resetpasswordcode', methods=["POST"])
def reset_password_code():
    db = User()
    if(db != None):
        email = str(request.json['email'])
        code = str(request.json['code'])
        # print(email)
        # newPassword = str(request.json['password'])
        print(db.get_code(email))
        if db.get_code(email)[2] == code:
            return {'response': 'success'}, 200
        else:
            return {'response': 'failed'}, 400
    else:
        return {'response': 'failed'}, 400


@app.route('/sendEmail', methods=["POST"])
def sendEmail():
    db = User()
    if(db != None):
        email = request.json["email"]
        print(db.getUserWithEmail(email))
        if db.getUserWithEmail(email) is None:
            code = str(random.randint(1000, 9999))
            db.insert_code(email, code)
            message = """\
                Image Converter Activation Code

                Welcome to the Image Converter!
                Please provide us with feedback after using the system.

                Here is your activation code: """
            message += code
            sendEmail = Email()
            sendEmail.sendMessage(email, message)
            print("sent")
            return {'response': 'success'}, 200
        else:
            return {'response': 'User Exists'}, 400
    else:
        return {{'response': 'failed'}}, 400

@app.route('/resetpasswordemail', methods=["POST"])
def resetPasswordEmail():
    db = User()
    if(db != None):
        email = str(request.json["email"])
        # print(db.getUserWithEmail(email))
        if db.getUserWithEmail(email) is not None:
            code = str(random.randint(1000, 9999))
            db.insert_code(email, code)
            message = """\
                Image Converter Reset Password Code

                Please provide us with feedback after using the system.

                Here is your reset password code: """
            message += code
            sendEmail = Email()
            sendEmail.sendMessage(email, message)
            print("sent")
            return jsonify({'response': 'success'})
        else:
            print("Errror")
            return {'response': 'User Exists'}, 200
    else:
        return {{'response': 'failed'}}, 400

@app.route('/bargraph', methods=['POST'])
@token
def barGraph():
    
    db = User()
    if(db != None):
        print("barGraph Working")
        label_1 = request.json['label_1']
        label_value_1 = request.json['label_value_1']
    #     if(db.login(username,password)):
    #         token = jwt.encode({'email': username, 'exp': datetime.datetime.utcnow(
    #         ) + datetime.timedelta(hours=2)}, 'secret', algorithm="HS256")
    #         result = "success"
    #         return jsonify({'result': result, 'token': str(token)})
    #     else:
    #         return jsonify({'result': 'failed'})
    # else:
    #     return {'response': 'failed'}, 400
        return jsonify({'response': 'success'})
    else:
        return {'response': 'failed'}, 400
 




if __name__ == '__main__':
    app.run(debug=True)
