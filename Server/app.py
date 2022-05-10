from flask import Flask
from flask import Response
import base64


app = Flask(__name__)

@app.route('/picture')
def index(picture):
    if picture is not None:
        # convert picture to base64
        picture = picture.decode('utf-8')

        return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)