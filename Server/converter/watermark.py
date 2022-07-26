from PIL import Image
import numpy as np
import cv2
import os
import base64

class AddMark:

    def __init__ (self,uploaded_image):
        self.img = uploaded_image

    def Dev(self):
        # Getting the height and width of the image
        width, height = self.img.size

        size = (100, 100)
        logo = Image.open('logo/logo-test.png')

        # You can use resize method here instead of
        # thumbnail method
        logo.thumbnail(size)

        # Location where we want to paste it on the
        # main image
        x = width - 100 - 10
        y = height - 100 - 0

        self.img.paste(logo, (x, y))
        return self.img

if __name__ == '__main__':
    obj = AddMark(Image.open('images/bar3.jpg'))

    obj.Dev()