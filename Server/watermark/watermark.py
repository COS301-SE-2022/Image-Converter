# from PIL import Image, ImageDraw, ImageFont
# from tkinter import filedialog
# from tkinter import Tk
# import os


# root = Tk()
# root.withdraw()
# filename = filedialog.askopenfilename(initialdir='C:\\Users\\Mama Modiselle\\Pictures\\example', title='Select Image')

import cv2
import numpy as np

mark = cv2.imread("watermark.jpg")
h_mark, w_mark, _ = mark.shape


img = cv2.imread('assets/barchart.jpg')
h_img, w_img, _ = img.shape

print(h_img, w_img)

centre_y = int(h_img / 2)
centre_x = int(w_img / 2)
top_y = centre_y - (h_mark / 2)
left_x = centre_x - int(w_mark / 2)
bottom_y = top_y + h_mark
right_x = left_x + w_mark

# cv2.circle(img, (left_x, top_y), 10, (0, 255, 0), -1)#comment out

#region of interest
img[top_y: bottom_y, left_x: right_x]

cv2.imshow("Img", img)
cv2.imshow("logo", mark)
cv2.waitKey(0)