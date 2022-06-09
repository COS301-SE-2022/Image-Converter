import datetime
from functools import wraps
import jwt
from flask import Flask,json,jsonify, request
from database.database import User
from flask import Response
from flask_cors import CORS
import base64


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
    db=User()
    if(db!=None):
        picture = request.json['picture']
        if picture is not None:

            base64_picture=base64.b64encode((bytes(picture[picture.find(",")+1:].encode('utf-8'))))
            imageReturned = "data:image/png;base64,"
            with open("images/download.png", "rb") as img_file:
                b64picture = base64.b64encode(img_file.read())
            image_converted = bytearray(b64picture)
            image_uploaded = bytearray(base64_picture)
            # if(db.insert_image(picture, image_converted, user[0])):
            #     print("Image inserted")

            db_image = db.get_image(user[0])

        return jsonify({'image': str(imageReturned+ bytes(db_image[4]).decode('UTF-8'))})
    else:
        return {'response': 'failed'}, 400


@app.route('/login' ,methods =['POST'])
def auth_login():
    db=User()
    if(db!=None):
        username = str(request.json['email'])
        password = str(request.json['password'])
        print(db.getUserWithEmail(username)[0])
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

if __name__ == '__main__':
    app.run(debug=True)