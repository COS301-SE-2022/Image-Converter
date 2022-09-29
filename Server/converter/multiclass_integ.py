import tensorflow as tf
import os
import cv2
import numpy as np
from keras.models import load_model
from numpy import byte
import tensorflow as tf
import base64


class MultiClassification:
    def __init__(self,uploaded_image):
        sliced_png = uploaded_image[22:]

        converted_base64= bytes(sliced_png, encoding='utf8')
        with open("img.png", "wb") as fh:
            fh.write((base64.decodebytes(converted_base64)))
        self.uploaded_image = 'img.png'
        self.graphType = ""
        self.match()



    def match(self):

        img_height = 90
        img_width = 90

        image=cv2.imread(self.uploaded_image)
        image_resized= cv2.resize(image, (img_height,img_width))
        image=np.expand_dims(image_resized,axis=0)


        model = tf.keras.models.load_model('model') 
        class_names = ['bar graph', 'flow chart', 'line graph', 'unrecognized', 'pie chart', 'table']

        pred=model.predict(image)

        output_class=class_names[np.argmax(pred)]
        self.graphType = output_class
        return self.graphType
        