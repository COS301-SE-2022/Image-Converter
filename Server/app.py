import datetime
from functools import wraps
from lib2to3.pytree import Node
from attr import s
import jwt
from flask import Flask, json, jsonify, render_template, request, session
from converter.graphPloting import GraphPloting
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

"""
Methos for creating a new token or checking if a token is valid.

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

"""
    Upload image Function:
        Classifies , cleans and add water mark to the image
    Parameters:
        User array
    HTTP method: POST
    Request data:
        picture
    Returns:
        JSON Object
"""

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
            print("#########################################")
            print(img_class.graphType)
            print("#########################################")

            imageCleaner = smoothing(opencv_img)

            imageResult =imageCleaner.clean_noise()
            if(db.insert_image(opencv_img, imageResult, user[0],img_class.graphType)):
                print("Image inserted")
            db_image = db.get_image(user[0])
            graphType = "This "+img_class.graphType
            conv=ConvertFomat()
            conv.covertImgFormat(db_image[4])
            return jsonify({'image': db_image[4], 'png':conv.getPng(),'jpg':conv.getJpg(), 'graphType': graphType})
        else:
            print("picture is None")
            return {'response': 'Picture is None!'},200
    else:
        return {'response': 'failed'}, 400


"""
    Login Function:
        logs the user into the system
    Parameters:
        None
    HTTP method: POST
    Request data:
        email, password
    Returns:
        JSON Object
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
            print(result)
            return jsonify({'response': result, 'token': str(token)})
        else:
            return {'response': 'failed'},200
    else:
        return {'response': 'failed'}, 400



"""
    Register Function:
        registers the user into the system
    Parameters:
        None
    HTTP method: POST
    Request data:
        name, surname, email, password and the verification code
    Returns:
        JSON Object
"""

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
            return {'response': 'code not found'}, 200
    else:
            return {'response': 'failed'}, 400


"""
    UploadHistory Function:
        Gets the 6 recent uploads for a specific user
    Parameters:
        User array
    HTTP method: GET
    Returns:
        JSON Object
"""
@app.route('/uploadhistory', methods=["GET"])
@token
def uploadhistory(user):
    db = User()
    if(db != None):
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


"""
    DeleteHistory Function:
        deletes a specific user history
    Parameters:
        None
    HTTP method: POST
    Request data:
        index for the specific history
    Returns:
        JSON Object
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
            return {'response': 'index is invalid'}, 400
    else:
        return {'response': 'failed'}, 400


"""
    UserFeedback Function:
        adds the user feedback in the data
    Parameters:
        User array
    HTTP method: POST
    Request data:
        feedback
    Returns:
        JSON Object
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


"""
    ResetPassword Function:
        updates the user password
    Parameters:
        None
    HTTP method: POST
    Request data:
        email, password
    Returns:
        JSON Object
"""
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


"""
    ResetPasswordCode Function:
        checks the verification code if it's valid
    Parameters:
        None
    HTTP method: POST
    Request data:
        email, verification code
    Returns:
        JSON Object
"""
@app.route('/resetpasswordcode', methods=["POST"])
def reset_password_code():
    db = User()
    if(db != None):
        email = str(request.json['email'])
        code = str(request.json['code'])
        print(db.get_code(email))
        if db.get_code(email)[2] == code:
            return {'response': 'success'}, 200
        else:
            return {'response': 'failed'}, 400
    else:
        return {'response': 'failed'}, 400


"""
    SendEmail Function:
        sending email with a verification code to the new user
    Parameters:
        None
    HTTP method: POST
    Request data:
        email
    Returns:
        JSON Object
"""
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


"""
    ResetPasswordEmail Function:
        sending email with a reset password verification code to a user
    Parameters:
        None
    HTTP method: POST
    Request data:
        email
    Returns:
        JSON Object
"""
@app.route('/resetpasswordemail', methods=["POST"])
def resetPasswordEmail():
    db = User()
    if(db != None):
        email = str(request.json["email"])
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


"""
    PlotGraph Function:
        plots a graph given a formula
    Parameters:
        User array 
    HTTP method: POST
    Request data:
        formula
    Returns:
        JSON Object
"""
@app.route('/plotting', methods=['POST'])
@token
def plot_graph(user):
    db=User()
    if(db!=None):
        formula = str(request.json['formula'])
        # print(picture)
        if formula is not None:
            graph = GraphPloting()
            image_converted=graph.draw(formula)
            if(db.insert_image(image_converted, image_converted, user[0],'line graph')):
                print("Image inserted")
            db_image = db.get_image(user[0])
            print(db_image[4])
        return jsonify({'image': db_image[4]})
    else:
        return {'response': 'failed'}, 400


"""
    unrecognizedGraphs Function:
        Gets all the unrecognized graphs (Only admin users)
    Parameters:
        User array
    HTTP method: GET
    Returns:
        JSON Object
"""
@app.route('/unrecognizedgraphs', methods=["GET"])
@token
def unrecognizedGraphs(user):
    db = User()
    if(db != None):
        if(user[6]):
            db_image_array=db.getUnrecognizedImages()
            OriginalImagelist=[]
            IndexArray=[]
            proccesedImagelist=[]
            for x in db_image_array:
                IndexArray.append(x[0])
                OriginalImagelist.append(x[3]) 
                proccesedImagelist.append(x[4]) 
            return jsonify({"OriginalImage": OriginalImagelist,"proccesedImage": proccesedImagelist ,"Index":IndexArray})
        return {'response':'UserNotAdmin'},200
    else:
        return {'response': 'failed'}, 400

"""
    AdminFeedback Function:
        the admin updates the graph type for a 
    Parameters:
        User array
    HTTP method: POST
    Request data:
        feedback
        index
    Returns:
        JSON Object
"""
@app.route('/adminFeedback' ,methods =['POST'])
@token
def adminFeedback(user):
    db=User()
    if(db!=None):
        feedback = request.json['feedback']
        index = request.json['index']
        if feedback is not None:
            if db.updateGraphType(feedback,index) is True:
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
