import datetime
from functools import wraps
import jwt
from flask import Flask, json, jsonify, render_template, request
from converter.smoothing import smoothing
from converter.templateMatching import Matching
from database.database import User
from flask import Response
from flask_cors import CORS
import base64
import cv2
import os
import io
import PIL.Image as Image
import numpy as np

app = Flask(__name__)

CORS(app)

# function to retrieve tokens


def token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = None
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            print(token)
            # alert when token is not found
            return jsonify({'result': 'Token is not found or invalid!'}), 401

        try:
            db = User()
            data = jwt.decode(token, 'secret', "HS256")
            # retrieve user with specific email
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
def upload_image(user): #processing on uploaded image 
    db = User()
    if(db != None):
        picture = request.json['picture']
        if picture is not None:
            # print("picture is not None")
            base64_picture = base64.b64encode(
                (bytes(picture[picture.find(",")+1:].encode('utf-8'))))  # convert image to base 64
            imageReturned = "data:image/png;base64,"
            imgdata = base64.b64decode(str(picture[picture.find(",")+1:]))
            img = Image.open(io.BytesIO(imgdata))
            opencv_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

            image_uploaded = bytearray(base64_picture)

            print(type(opencv_img))
            templateMatch = Matching(opencv_img) #template matching functionality
            print(templateMatch.graphType)
            print(templateMatch.perfectMatch)
            imageCleaner = smoothing(opencv_img) #image smoothing functionality
            imageCleaner.clean_noise()
            with open("images/original/Graph.png", "rb") as img_file:
                b64picture = base64.b64encode(img_file.read())
            print("b64picture")
            image_converted = bytearray(b64picture)
            if(db.insert_image(picture, image_converted, user[0])):
                print("Image inserted")
            db_image = db.get_image(user[0])
            print(db_image)
        return jsonify({'image': str(imageReturned + bytes(db_image[4]).decode('UTF-8'))})
    else:
        return {'response': 'failed'}, 400

    # db=User()
    # if(db!=None):
    #     picture = request.json['picture']
    #     if picture is not None:

    #         base64_picture=base64.b64encode((bytes(picture[picture.find(",")+1:].encode('utf-8'))))
    #         imageReturned = "data:image/png;base64,"
    #         with open("images/download.png", "rb") as img_file:
    #             b64picture = base64.b64encode(img_file.read())
    #         image_converted = bytearray(b64picture)
    #         image_uploaded = bytearray(base64_picture)
    #         # if(db.insert_image(picture, image_converted, user[0])):
    #         #     print("Image inserted")

    #         db_image = db.get_image(user[0])

    #     return jsonify({'image': str(imageReturned+ bytes(db_image[4]).decode('UTF-8'))})
    # else:
    #     return {'response': 'failed'}, 400


@app.route('/login', methods=['POST'])
def auth_login():  # authourising user login function
    db = User()
    if(db != None):
        username = str(request.json['email'])  # retrieve email and password
        password = str(request.json['password'])
        print(db.getUserWithEmail(username)[0])
        if(db.login(username, password)):  # assign token to user upon login
            token = jwt.encode({'email': username, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(hours=2)}, 'secret', algorithm="HS256")
            result = "success"
            return jsonify({'result': result, 'token': str(token)})
        else:
            return jsonify({'result': 'failed'})
    else:
        # status code and error response if user login failed
        return {'response': 'failed'}, 400



#user registration functionality
@app.route('/register', methods=["POST"])
def register():
    db = User()
    if(db != None):
        # retrieve username, surname, email and password
        name = str(request.json["name"])
        surname = str(request.json["surname"])
        email = str(request.json["email"])
        password = str(request.json["password"])
        if(db.register(name, surname, email, password)):  # verify registration based on parameters
            token = jwt.encode({'email': email, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(hours=2)}, 'secret', algorithm="HS256")
            result = "success"
            return jsonify({'result': result, 'token': str(token)})
        else:
            return {'response': 'failed'}, 400
    else:
        # status code and error response if user login failed
        return {'response': 'failed'}, 400


@app.route('/template')
def img():
    return render_template('index.html', images=True)


@app.route('/uploadhistory', methods=["GET"])
@token
def uploadhistory(user):  # user upload history functionality

    db = User()
    if(db != None):
        imageReturned = "data:image/png;base64,"
        db_image_array = db.get_image_history(user[0])
        OriginalImagelist = []  # array to hold original uploaded images
        IndexArray = []
        proccesedImagelist = []  # array to hold proccessed images
        for x in db_image_array:
            IndexArray.append(x[0])
            OriginalImagelist.append(str(bytes(x[3]).decode('UTF-8')))
            proccesedImagelist.append(
                str(imageReturned + bytes(x[4]).decode('UTF-8')))

        return jsonify({"OriginalImage": OriginalImagelist, "proccesedImage": proccesedImagelist, "Index": IndexArray})
    else:
        return {'response': 'failed'}, 400  # database does not exist


@app.route('/deletehistory', methods=['POST'])
@token
def delete_user_history(user):  # deleting image from user history
    db = User()
    if(db != None):
        index = request.json['index']
        print(index)
        if index is not None:
            # deleting image from database for delete from history feature
            if db.delete_history(index) is True:
                print("Image deleted")
                # response upon successful deletion
                return jsonify({'response': 'success'})
            else:
                return jsonify({'response': 'failed'})
        else:
            return {'response': 'failed'}, 400
    else:
        # response when database is does not exist
        return {'response': 'failed'}, 400


if __name__ == '__main__':
    app.run(debug=True)
