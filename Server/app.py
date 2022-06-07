import datetime
from functools import wraps
import jwt
from flask import Flask,json,jsonify, render_template, request
from converter.smoothing import smoothing
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

def token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user=None
        token= None
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

@app.route('/picture' ,methods =['POST'])
@token
def upload_image(user):
    picture = request.json['picture']
    if picture is not None:
        # print("picture is not None")
        base64_picture=base64.b64encode((bytes(picture[picture.find(",")+1:].encode('utf-8'))))
        imageReturned = "data:image/png;base64,"
        imgdata = base64.b64decode(str(picture[picture.find(",")+1:]))
        img = Image.open(io.BytesIO(imgdata))
        opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        # bytes = readimage(picture)
        # image = Image.open(io.BytesIO(bytearray(base64_picture) ))
        cv2.imshow("IMAGE_RESULT", opencv_img)
        print(type(opencv_img))
        imageCleaner = smoothing(opencv_img)
        cleaned_image = imageCleaner.clean_noise()
        # cv2.imshow("IMAGE_RESULT", opencv_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        b64picture = base64.b64encode(cleaned_image.tobytes())
        print(type(b64picture))
        # print(b64picture)
        # with open("images/download.png", "rb") as img_file:
        #     b64picture = base64.b64encode(img_file.read())
        # print("b64picture")

    return jsonify({'image': str(imageReturned+ cleaned_image.tobytes().decode('UTF-8'))})


@app.route('/login' ,methods =['POST'])
def auth_login():
    db=User()
    if(db!=None):
        username = str(request.json['email'])
        password = str(request.json['password'])
        if(db.login(username,password)):
            token = jwt.encode({'email': username, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(hours=2)}, 'secret', algorithm="HS256")
            result = "success"
            return jsonify({'result': result,'token':str(token)})
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
        if(db.register(name, surname, email, password)):
            return {'response': 'registered'}, 200
        else:
            return {'response': 'failed'}, 400
    else:
            return {'response': 'failed'}, 400

@app.route('/template')
def img():
    return render_template('index.html', images = True)


if __name__ == '__main__':
    app.run(debug=True)