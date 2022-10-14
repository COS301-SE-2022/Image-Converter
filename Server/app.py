import datetime
from functools import wraps
from lib2to3.pytree import Node
from typing import final
import jwt
from flask import Flask, json, jsonify, render_template, request, session
from converter.resizing import imageResizing
from converter.graphPloting import GraphPloting
from converter.smoothing import smoothing
from converter.multiclass_integ import MultiClassification
from converter.model_training import trainModel
from database.database import User
from database.sendEmail import Email
from converter.ConvertFomat import ConvertFomat
from converter.watermark import AddMark
from flask import Response
from flask_cors import CORS
import base64
import cv2
import random
import io
import PIL.Image as Image
import numpy as np
import urllib.request
import uuid
from PIL import Image



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
            db.incrementActivity("Uploads")
            base64_picture=base64.b64encode((bytes(picture[picture.find(",")+1:].encode('utf-8'))))
            imageReturned = "data:image/png;base64,"
            imgdata = base64.b64decode(str(picture[picture.find(",")+1:]))
            
            img = Image.open(io.BytesIO(imgdata))
            opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
            
            image_uploaded = bytearray(base64_picture)
            img_class = MultiClassification(picture)
            print("#########################################")
            print(img_class.graphType)
           
            print("#########################################")

            imageCleaner = smoothing(opencv_img)
            imageResult =imageCleaner.clean_noise()
            imageHeight = imageCleaner.height
            imageWidth = imageCleaner.width
            print(imageHeight, ", ", imageWidth)
            if(db.insert_image(opencv_img, imageResult, user[0],"")):
                print("Image inserted")
            db_image = db.get_image(user[0])
            if(img_class.graphType=="unrecognized"):
                db.incrementActivity("Unrecognized")
                graphType = "This is an "+img_class.graphType+" graph"
            else:
                graphType = "This is a "+img_class.graphType
            conv=ConvertFomat()
            conv.covertImgFormat(db_image[4])
            return jsonify({'image': db_image[4], 'png':conv.getPng(),'jpg':conv.getJpg(), 'graphType': graphType,'id':db_image[0], 'imageHeight': imageHeight, 'imageWidth': imageWidth})
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
        if db.getUserWithEmail(username) is not None:
            if(db.login(username,password)):
                token = jwt.encode({'email': username, 'exp': datetime.datetime.utcnow(
                ) + datetime.timedelta(hours=2)}, 'secret', algorithm="HS256")
                result = "success"
                print(result)
                return jsonify({'response': result, 'token': str(token)})
            else:
                return {'response': 'failed'},200
        else:
            return {'response': 'UserDoesNotExist'},200
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
            db_image_array=db.getUnrecognizedImages()
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
    deleteUnrecognisableImage Function:
        Deletes a specific image from the list unrecognisable images.
    Parameters:
        User array
    HTTP method: GET
    Request data:
        index for the specific unrecognisable image
    Returns:
        JSON Object
"""
@app.route('/deleteUnrecognisableImage', methods=["POST"])
@token
def deleteUnrecognisableImage(user):
    db = User()
    if(db != None):
        if(user[6]):
            index = request.json['index']
            if index is not None:
                if db.deleteUnrecognizedImages(index) is True:
                    print("Image deleted")
                    db.decrementActivity("Unrecognized")
                    return jsonify({'response': 'success'})
                else:
                    print("Image not deleted")
                    return jsonify({'response': 'failed'})
            else:
                return {'response': 'index is invalid'}, 400
        return {'response':'UserNotAdmin'},200

@app.route('/checkusertype', methods=['GET'])
@token
def check_user(user):
    db=User()
    if(db!=None):
        return jsonify({'response':'success','userType': 'true'})
    else:
        return {'response': 'failed'}, 400

"""
    addWaterMark Function:
        Resizes the image to 800x800 and adds the water mark to the image
    Parameters:
        User array
    HTTP method: POST
    Request data:
        picture
    Returns:
        JSON Object
"""
@app.route('/addWatermark', methods=['POST'])
@token
def addWatermark(user):
    db=User()
    if(db!=None):
        picture = request.json['picture']
        # print(picture)
        if picture is not None:
            print("picture is not None")
            imgdata = base64.b64decode(str(picture[picture.find(",")+1:]))
            img = Image.open(io.BytesIO(imgdata))
            opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
            
            resize = imageResizing(opencv_img)
            resizedImage = resize.resize()
            logo = AddMark(Image.fromarray(cv2.cvtColor(resizedImage, cv2.COLOR_BGR2RGB)))
            imageResult = logo.Dev()
            
            buffered = io.BytesIO()
            imageResult.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue())
            img_base64 = bytes("data:image/png;base64,", encoding='utf-8') + img_str
            return jsonify({'image': img_base64.decode('utf-8')})
        else:
            print("picture is None")
            return {'response': 'Picture is None!'},200
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
        image = request.json['image']
        print(image)
        myUUID = str(uuid.uuid4())
        if(feedback=="straight line"):
            urllib.request.urlretrieve(image,"./graph_dataset/line_graph/"+feedback+'_'+myUUID+"img.png")
        elif(feedback=="bar graph"):
            urllib.request.urlretrieve(image,"./graph_dataset/bar_chart/"+feedback+'_'+myUUID+"img.png")
        elif(feedback=="pie chart"):
            urllib.request.urlretrieve(image,"./graph_dataset/pie_chart/"+feedback+'_'+myUUID+"img.png")
        if feedback is not None:
            if db.updateGraphType(feedback,index) is True:
                db.decrementActivity("Unrecognized")
                print("feedback inserted")
                return jsonify({'response': 'success'})
            else:
                return jsonify({'response': 'failed'})
        else:
            return {'response': 'failed'}, 400
    else:
        return {'response': 'failed'}, 400


"""
    IncrementActivity Function:
        It increments the number of times an activity is done
    Parameters:
        None
    HTTP method: POST
    Request data:
        acivity
    Returns:
        JSON Object
"""
@app.route('/incrementActivity' ,methods =['POST'])
@token
def incrementActivity(user):
    db=User()
    if(db!=None):
        
        activity = request.json['activity']
        if activity is not None:
            if db.incrementActivity(activity) is True:
                return jsonify({'response': 'success'})
            else:
                return jsonify({'response': 'failed'})
        else:
            return {'response': 'failed'}, 400
    else:
        return {'response': 'failed'}, 400


"""
    Activities Function:
        It increments the number of times an activity is done
    Parameters:
        None
    HTTP method: GET
    Returns:
        JSON Object
"""
@app.route('/activities' ,methods =['GET'])
@token
def Activities(user):
    db=User()
    if(db!=None):
        data= db.getActivities()
        return jsonify({data[0][1]: data[0][2],data[1][1]: data[1][2] ,data[2][1]:data[2][2]})
    else:
        return {'response': 'failed'}, 400

# @app.route('/imageAnnotation' ,methods =['POST'])
# @token
# def imageAnnotation(user):
#     db=User()
#     if(db!=None):
#         feedback = request.json['feedback']
#         if feedback is not None:
#             print(feedback)
#             return jsonify({'response': 'success'})
#         else:
#             return {'response': 'failed'}, 400
#     else:
#         return {'response': 'failed'}, 400
"""
    graphs Function:
        Get graphs of the same types
    Parameters:
        User array
    HTTP method: POST
    Returns:
        JSON Object
"""
@app.route('/graphs', methods=["POST"])
@token
def graphs(user):
    db = User()
    if(db != None):
            graphType = request.json['graphType']
            db_image_array=db.getGraph(graphType)
            OriginalImagelist=[]
            Comments=[]
            IndexArray=[]
            proccesedImagelist=[]
            for x in db_image_array:
                IndexArray.append(x[0])
                
                OriginalImagelist.append(x[3]) 
                proccesedImagelist.append(x[4]) 
                Comments.append(x[5])
            return jsonify({"OriginalImage": OriginalImagelist,"proccesedImage": proccesedImagelist ,"Index":IndexArray,"Comments":Comments})
    else:
        return {'response': 'failed'}, 400

"""
    Comment Function:
        adds the user's comment to the database
    Parameters:
        User array
    HTTP method: POST
    Request data:
        comment
    Returns:
        JSON Object
"""
@app.route('/comment' ,methods =['POST'])
@token
def user_comment(user):
    db=User()
    if(db!=None):
        comment = request.json['comment']
        index = request.json['index']
        if comment is not None:
            if db.insert_comment(index, comment) is True:
                print("comment inserted")
                return jsonify({'response': 'success'})
            else:
                return jsonify({'response': 'failed'})
        else:
            return {'response': 'failed'}, 400
    else:
        return {'response': 'failed'}, 400


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
