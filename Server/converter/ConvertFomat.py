from io import BytesIO
from PIL import Image
from flask import jsonify
import requests
import base64

class ConvertFomat:
    def __init__(self):
        self.png=""
        self.jpg=""

    def covertImgFormat(self,imageLnk):
        #url="https://storage.googleapis.com/hardcode-9aba7.appspot.com/2Original.jpg?Expires=1688848151&GoogleAccessId=firebase-adminsdk-fdx52%40hardcode-9aba7.iam.gserviceaccount.com&Signature=lI4zRZtNhYhJglrFvayk%2BVqPSbJGdvH9w504Uhj2D9wadrwZC2lpQg9WcQeVxvgjYPgsgUp%2Fbz6xcmZcorGM65iYKNDQ1Knt6edNF4gHoB7irtCdGktLfrOr3ZlER8PS5qizaXE%2BZw%2F89dCQraodXjFnj5FChOjGo4SJR0nUJ4uElTD0Rfigv48jG84DWgSw1jtn%2BpRESQGL6WRCPUcGNERmMG7NXTFweQ0zBZ4EHQ7MNSqPZHO%2F0CHCfmfDnbzynguYXcsFLBXx55c5D%2BEY6y2d38dIT2EE7NGLLOQEfCQQbQkNJI2DuDJyDYONOhN1LbnJ%2F18s4FCiFjyZAfaSLA%3D%3D"
        response = requests.get(imageLnk)
        im = Image.open(BytesIO(response.content))
        rgb_im = im.convert('RGB')
        rgb_im.save('processedImg.jpg')
        rgb_im.save('processedImg.png')

        with open("processedImg.png", "rb") as img_file:
            convPng = base64.b64encode(img_file.read())
        with open("processedImg.jpg", "rb") as img_file:
            cnvJpg = base64.b64encode(img_file.read())

        self.png=str("data:image/png;base64,"+ bytes(convPng).decode('UTF-8'))
        self.jpg=str("data:image/jpg;base64,"+ bytes(cnvJpg).decode('UTF-8'))
        
    def getPng(self):
        return self.png
    
    def getJpg(self):
        return self.jpg