import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

data_dir = "imageSmoothing"

for img in os.listdir( data_dir + "/graphs"):
    img_array = cv2.imread(data_dir + "/graphs/" + img)
    
    img_array = cv2.resize(img_array, (128,128))
    lr_img_array = cv2.resize(img_array,(32,32))
    cv2.imwrite(data_dir+ "/hr_images/" + img, img_array)
    cv2.imwrite(data_dir+ "/lr_images/"+ img, lr_img_array)
