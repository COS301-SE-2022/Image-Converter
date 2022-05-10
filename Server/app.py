from flask import Flask,json,jsonify
from flask import Response
import base64


app = Flask(__name__)

@app.route('/picture' ,methods =['POST'])
def upload_image():
    with open("images/image1.jpg", "rb") as img_file:
        b64picture = base64.b64encode(img_file.read())
    # print(b64picture)

    return jsonify({'response': str(b64picture)})

    
@app.route('/')
def index():
    return "Hello World!"



if __name__ == '__main__':
    app.run(debug=True)