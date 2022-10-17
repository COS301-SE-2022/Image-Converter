import cv2
import numpy as np
from converter.watermark import AddMark
from converter.resizing import imageResizing
from PIL import Image
import sys
import app
sys.path.append('../')

class smoothing:
    def __init__(self,uploaded_image):
        self.img = uploaded_image

    def clean_noise(self):
        #Image smoothing and sharpening
        app.socketio.emit('data-tmp',"Image is getting cleaned")
        blurred = cv2.bilateralFilter(self.img, 15, 75, 75)
        sharp = cv2.addWeighted(self.img, 3.5, blurred, -2.1, 0)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        open = cv2.morphologyEx(sharp, cv2.MORPH_OPEN, kernel, iterations=1)

        #Resizing the image
        app.socketio.emit('data-tmp',"Image is getting resized")
        resizedImage = imageResizing(open)
        resizedImage = resizedImage.resize()
        print('Resized image:', resizedImage.shape)

        #Adding a watermark to the image
        app.socketio.emit('data-tmp',"Adding watermark to the image")
        imageWatermark = AddMark(Image.fromarray(cv2.cvtColor(resizedImage, cv2.COLOR_BGR2RGB)))
        imageWatermark = imageWatermark.Dev()

        #Converting the returned image to numpy array
        cleanedImage = np.array(imageWatermark) 
        cleanedImage = cleanedImage[:, :, ::-1].copy() 


        cv2.imwrite("./../images/original/Graph.png", cleanedImage)
        return cleanedImage

if __name__ == '__main__':
    src = 'barGraph.jpeg'
    img = cv2.imread(src)
    object = smoothing(img)
    object.clean_noise()