import cv2
from numpy import byte
import tensorflow as tf
import os
import base64


class Classification:
    def __init__(self,uploaded_image):
        # print("====================")
        sliced_png = uploaded_image[22:]
        # print(uploaded_image[22:])
        # print("============")

        converted_base64= bytes(sliced_png, encoding='utf8')
        with open("img.png", "wb") as fh:
            fh.write((base64.decodebytes(converted_base64)))
        self.uploaded_image = 'img.png'
        # print("=======")
        # print(self.uploaded_image[21:])
        # print("=======")
        self.graphType = ""
        self.match()



    def match(self):
  
        img_pred =[]
       
        ##################################################################################
        ## Pie vs Line
        ##################################################################################

        CATEGORIES = ["pie_chart", "line_graph"]


        def prepare(filepath):
            IMG_SIZE = 100  # 50 in txt-based
            img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

        model = tf.keras.models.load_model('Pie_v_Line-CNN.model')

        prediction = model.predict([prepare(self.uploaded_image)])

        img_pred.append(CATEGORIES[int(prediction[0][0])])


        ##################################################################################
        ## Pie vs Bar
        ##################################################################################


        CATEGORIES2 = ["pie_chart", "bar_chart"]

        def prepare(filepath):
            IMG_SIZE = 100  # 50 in txt-based
            img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


        model = tf.keras.models.load_model('Pie_v_Bar-CNN.model')

        prediction = model.predict([prepare(self.uploaded_image)])

        img_pred.append(CATEGORIES2[int(prediction[0][0])])

        ##################################################################################
        ## Bar vs Line
        ##################################################################################


        CATEGORIES3 = ["bar_chart", "line_graph"]

        def prepare(filepath):
            IMG_SIZE = 100  # 50 in txt-based
            img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


        model = tf.keras.models.load_model('Bar_v_Line-CNN.model')

        prediction = model.predict([prepare(self.uploaded_image)])

        img_pred.append(CATEGORIES3[int(prediction[0][0])])

        print(img_pred)

        if(img_pred.count("bar_chart") ==2):
            self.graphType = "bar chart"
            return self.graphType
        elif((img_pred.count("line_graph") ==2)):
            self.graphType = "line graph"
            return self.graphType
        elif((img_pred.count("pie_chart") ==2)):
            self.graphType = "pie chart"
            return self.graphType
