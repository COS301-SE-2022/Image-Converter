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
        imageReturned = "data:image/png;base64,"
        with open("images/image1.jpg", "rb") as img_file:
            b64picture = base64.b64encode(img_file.read())
        print("b64picture")

    return jsonify({'image': str(imageReturned+ b64picture.decode('UTF-8'))})

    
@app.route('/')
def index():
    return "Hello World!"

@app.route('/login', methods=["POST"])
def login():
    db = app.config['DATABASE']
    

if __name__ == '__main__':
    app.run(debug=True)