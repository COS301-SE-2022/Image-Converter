import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

data_dir = "graphs"
home = "imageSmoothing"

images = []
for filename in os.listdir(data_dir):
    img = cv2.imread(os.path.join(data_dir,filename))
    if img is not None:
        images.append(img)
        img_array = cv2.resize(img, (800,800))
        lr_img_array = cv2.resize(img_array,(32,32))
        cv2.imwrite(os.path.join("hr_images/",filename),img_array)
        cv2.imwrite(os.path.join("lr_images/",filename), lr_img_array)
print(len(images))

cv2.imshow('Test imageSmoothing', images[100])
cv2.waitKey(0)
cv2.destroyAllWindows()


# for img in os.listdir(data_dir):
#     img_array = cv2.imread(data_dir + img)
    
#     img_array = cv2.resize(img_array, (128,128))
#     lr_img_array = cv2.resize(img_array,(32,32))
#     cv2.imwrite(home + "/hr_images/" + img, img_array)
#     cv2.imwrite(home + "/lr_images/"+ img, lr_img_array)
