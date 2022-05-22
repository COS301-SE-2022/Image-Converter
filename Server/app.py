from flask import Flask,json,jsonify, request
from flask import Response
from flask_cors import CORS
import base64


app = Flask(__name__)

CORS(app)

@app.route('/picture' ,methods =['POST'])
def upload_image():
    picture = request.json['picture']
    if picture is not None:
        print("picture is not None")
        with open("images/image1.jpg", "rb") as img_file:
            b64picture = base64.b64encode(img_file.read())
        print("b64picture")

    return jsonify({'image': str(picture)})


@app.route('/login' ,methods =['POST'])
def auth_login():
    username = request.json['email']
    password = request.json['password']
    if username is not None and password is not None and username != "" and password:
        return jsonify({'Auth': '1'})
    else:
        return jsonify({'Auth': '0'})

@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)