from io import BytesIO
from PIL import Image
import requests
import base64

class ConvertFomat:
    #def __init__(self):
    def __init__(self):
        self.png=""
        self.jpg=""
        self.tif=""
        self.bmp=""

    def covertImgFormat(self,imageLnk):
        
        response = requests.get(imageLnk)
        im = Image.open(BytesIO(response.content))
        rgb_im = im.convert('RGB')
        rgb_im.save('processedImg.jpg')
        rgb_im.save('processedImg.png')
        rgb_im.save('processedImg.tiff')
        rgb_im.save('processedImg.bmp')
        rgb_im.save('processedImg.jfif')
        print("abv")

        with open("processedImg.png", "rb") as img_file:
            convPng = base64.b64encode(img_file.read())
        with open("processedImg.jpg", "rb") as img_file:
            cnvJpg = base64.b64encode(img_file.read())
        with open("processedImg.tiff", "rb") as img_file:
            cnvTiff = base64.b64encode(img_file.read())
        with open("processedImg.bmp", "rb") as img_file:
            cnvBmp = base64.b64encode(img_file.read())

        self.png=str("data:image/png;base64,"+ bytes(convPng).decode('UTF-8'))
        self.jpg=str("data:image/jpg;base64,"+ bytes(cnvJpg).decode('UTF-8'))
        self.tiff = str("data:image/tiff;base64," + bytes(cnvTiff).decode('UTF-8'))
        self.bmp = str("data:image/bmp;base64," + bytes(cnvTiff).decode('UTF-8'))

    def getPng(self):
        return self.png

    def getJpg(self):
        return self.jpg