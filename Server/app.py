import datetime
from functools import wraps
import jwt
from flask import Flask, json, jsonify, request
from database.database import User
from flask import Response
from flask_cors import CORS
import base64


app = Flask(__name__)

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
# @token
def upload_image():
    picture = request.json['picture']
    if picture is not None:
        # print("picture is not None")
        imageReturned = "data:image/png;base64,"
        with open("images/download.png", "rb") as img_file:
            b64picture = base64.b64encode(img_file.read())
        # print("b64picture")

    return jsonify({'image': str(imageReturned + b64picture.decode('UTF-8'))})


@app.route('/login', methods=['POST'])
def auth_login():
    db = User()
    if(db != None):
        username = str(request.json['email'])
        password = str(request.json['password'])
        if(db.login(username, password)):
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
        if(db.register(name, surname, email, password)):
            token = jwt.encode({'email': name, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(hours=2)}, 'secret', algorithm="HS256")
            result = "success"
            return jsonify({'result': result, 'token': str(token)})
        else:
            return {'response': 'failed'}, 400
    else:
        return {'response': 'failed'}, 400


if __name__ == '__main__':
    app.run(debug=True)
