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

"""
    token function:
        handles the functionality of the token assigned to eash user upon registering or login
    Parameters: 
        self (current instance), user id & feedback
    Returns: 
        decorated function  
"""
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


"""
     upload_image function:
        converts the uploaded image into a byte array for storage in the backend and applies the
        functionality of image smoothening and template matching 
      Parameters: 
          user
     Returns: 
        print out if the image was inserted successfully & also prints out the kind of graph identified by the template matcher
        also prints out an error 404 if the db does not exist
         
"""
@app.route('/picture', methods=['POST'])
@token
def upload_image(user):
    db=User()
    if(db!=None):
        picture = request.json['picture']
        if picture is not None:
            # print("picture is not None")
            base64_picture=base64.b64encode((bytes(picture[picture.find(",")+1:].encode('utf-8'))))
            imageReturned = "data:image/png;base64,"
            imgdata = base64.b64decode(str(picture[picture.find(",")+1:]))
            img = Image.open(io.BytesIO(imgdata))
            opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
            
            image_uploaded = bytearray(base64_picture)
            
            print(type(opencv_img))
            templateMatch = Matching(opencv_img)
            print(templateMatch.graphType)
            print(templateMatch.perfectMatch)
            imageCleaner = smoothing(opencv_img)
            imageCleaner.clean_noise()
            with open("images/original/Graph.png", "rb") as img_file:
                b64picture = base64.b64encode(img_file.read())
            print("b64picture")
            image_converted = bytearray(b64picture)
            if(db.insert_image(picture, image_converted, user[0])):
                print("Image inserted")
            db_image = db.get_image(user[0])
            print(db_image)
            graphType = "This graph is"
            if(templateMatch.perfectMatch>5):
                graphType = graphType + " a "+templateMatch.graphType
            else:
                graphType= graphType + " not recognized by the system"
        return jsonify({'image': str(imageReturned+ bytes(db_image[4]).decode('UTF-8')), 'graphType': graphType})
    else:
        return {'response': 'failed'}, 400

"""
    auth_login function:
        authorises the login functionality by assigning the access token given to a user 
    Parameters: 
        None
    Returns: 
        a success result & access token if the authorisation was successful, 
        otherwise it returna a failed result and a status error code 400  
"""
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


"""
    register function:
        performs the user registration functionality by retrieving the user's credentials from the form on the front-end
        this function also assigns an access token to each user
    Parameters: 
        None
    Returns: 
        a success result & the access token if the registration is successful.
        If the registration is unseccessful, then a failed response is returned and a status error code 400 
"""
@app.route('/register', methods=["POST"])
def register():
    db = User()
    if(db != None):
        name = str(request.json["name"])
        surname = str(request.json["surname"])
        email = str(request.json["email"])
        password = str(request.json["password"])
        if(db.register(name, surname, email, password)):
            token = jwt.encode({'email': email, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(hours=2)}, 'secret', algorithm="HS256")
            result = "success"
            return jsonify({'result': result, 'token': str(token)})
        else:
            return {'response': 'failed'}, 400
    else:
            return {'response': 'failed'}, 400

@app.route('/template')
def img():
    return render_template('index.html', images = True)


"""
    uploadhistory function:
        creates the arrays for storing the uploaded and converted images for each user for the upload history functionality
    Parameters: 
        None
    Returns: 
          a failed response is returned with a status error code 400 if the db does not exist
"""
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
            OriginalImagelist.append(str( bytes(x[3]).decode('UTF-8'))) 
            proccesedImagelist.append(str(imageReturned+ bytes(x[4]).decode('UTF-8'))) 


        return jsonify({"OriginalImage": OriginalImagelist,"proccesedImage": proccesedImagelist ,"Index":IndexArray})
    else:
        return {'response': 'failed'}, 400


"""
    delete_user_history function:
        performs the functionality of deleting the images if the database exists
    Parameters: 
        None
    Returns: 
        a success result & an appropriate message if printed.
        If the deletion is unseccessful, then a failed response is returned and a status error code 400 
"""
@app.route('/deletehistory' ,methods =['POST'])
@token
def delete_user_history(user):
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

"""
    user_feedback function:
        allows for the user feedback functionality to be performed if the database exists
    Parameters: 
        None
    Returns: 
        a success result & the access token if the feedback is submitted successfully, an appropriate string is also printed out.
        If the submission is unseccessful, then a failed response is returned and a status error code 400 
"""
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



if __name__ == '__main__':
    app.run(debug=True)