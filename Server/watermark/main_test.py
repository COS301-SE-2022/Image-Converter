# from watermark import AddMark

# AddMark.Dev()

# import cv2
from watermark import AddMark
from PIL import Image

# pic = cv2.imread('images/bar3.jpg')

obj = AddMark(Image.open('images/bar3.jpg'))

obj.Dev()
# print(obj.Dev())
