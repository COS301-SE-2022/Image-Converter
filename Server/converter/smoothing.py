import cv2
import numpy as np

class smoothing:
    def __init__(self,uploaded_image):
        # read image
        # self.img = cv2.imread('draw.jpeg')
        self.img = uploaded_image


    def clean_noise(self):
        # blur
        blur = cv2.medianBlur(self.img, 5)

        # convert to hsv and get saturation channel
        sat = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)[:,:,1]

        # threshold saturation channel
        thresh = cv2.threshold(sat, 50, 255, cv2.THRESH_BINARY)[1]

        # apply morphology close and open to make mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
        mask = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel, iterations=1)

        # write black to input image where mask is black
        img_result = self.img.copy()
        img_result[mask==0] = (255,255,255)

        # display it
        # cv2.imshow("IMAGE", self.img)
        print("printing image")
        cv2.imshow("IMAGE_RESULT", img_result)
        # cv2.imwrite("images/original/Graph.png", img_result)
        # image = cv2.imread('images/original/Graph.png')
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return img_result

