# from PIL import Image, ImageDraw, ImageFont
# from tkinter import filedialog
# from tkinter import Tk
# import os


# root = Tk()
# root.withdraw()
# filename = filedialog.askopenfilename(initialdir='C:\\Users\\Mama Modiselle\\Pictures\\example', title='Select Image')

import cv2
import numpy as np

logo = cv2.imread("watermark.jpg")

cv2.imshow("logo", logo)
cv2.waitKey(0)