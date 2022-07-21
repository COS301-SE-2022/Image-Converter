import cv2
import numpy as np
from resizing import imageResizing
from PIL import Image
import PIL

class smoothing:
    def __init__(self,uploaded_image):
        self.img = uploaded_image


    def clean_noise(self):
        # blur
        blur = cv2.bilateralFilter(self.img, 9, 75, 75)

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
        # print("printing image")
        # cv2.imshow("IMAGE_RESULT", img_result)

        #resizing
        cv2.imwrite("images/original/Graph.png", img_result)
        # k = Image.open('Server/images/original/Graph.png')
        object = imageResizing(Image.fromarray(img_result))
        img = object.resize()
        img = np.asarray(img)
        cv2.imwrite("images/original/Graph.png", img)
    
        image = cv2.imread('images/original/Graph.png')
        return img

if __name__ == '__main__':
    src = 'graph.jpeg'
    img = cv2.imread(src)
    object = smoothing(img)
    object.clean_noise()
    # images = ['barGraph.jpeg', 'balloons_noisy.png']
    # img = []
    # saturation = []
    # bilateralBlur = []
    # threshold = []
    
    # # print(img)

    # for i in range(len(images)):
    #     img.append(cv2.imread(images[i]))

    # #Applying the blurring algorithms
    # nums = [9, 15, 18, 21, 24, 27, 30]

    # for i in range(len(img)):
    #     bilateralBlur.append(cv2.bilateralFilter(img[i].copy(), 15, 75, 75))

    # kernel = np.array([[-1, -1, -1],
    #                    [-1, 9, -1],
    #                    [-1, -1, -1]])
    # for i in range(len(img)):
    #     saturation.append(cv2.filter2D(src=bilateralBlur[i], ddepth=-1, kernel=kernel))
    #     # threshold.append(cv2.filter2D(src=img[i].copy(), ddepth=-1, kernel=kernel))
    #     # bilateralBlur[i] = cv2.filter2D(img[i].copy(), -1, filter)

    
    # #apply morphology close and open
    # input = [3, 4, 5, 6, 9, 12, 15, 18]
    # close = []
    # open = []
    # th1 = []
    # th2 = []
    # th3 = []
    # th4 = []
    # th5 = []
    # img = img.img_to_array(img, dtype='uint8')

    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    # for i in range(len(bilateralBlur)): 
    #     th1.append(cv2.adaptiveThreshold(img[i], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4))
    #     close.append(cv2.morphologyEx(img[i], cv2.MORPH_CLOSE, kernel, iterations=1))
    #     open.append(cv2.morphologyEx(th3[i], cv2.MORPH_OPEN, kernel, iterations=1))
    # src = 'graph.jpeg'
    # img = cv2.imread(src)

    # # img = image.load_img('barGraph', grayscale=True, target_size=(224, 224))
    # # img = image.img_to_array(img, dtype='uint8')
    # blurred = cv2.bilateralFilter(img, 15, 75, 75)
    # sharp = cv2.addWeighted(img, 3.5, blurred, -2.1, 0)
    # gry = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    # adapt = cv2.adaptiveThreshold(gry, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 12)


    # for i in range(len(close)):
    #     cv2.imshow("Original_Image", img[i])
    #     # cv2.imshow("Close " + str(i), close[i])
    #     cv2.imshow("Open", open[i])
       
    #     cv2.imshow("th1", th1[i])
    #     cv2.imshow("th2", th2[i])
    #     cv2.imshow("th3", th3[i])
    #     cv2.imshow("th4", th4[i])
    #     cv2.imshow("th5", th5[i])
    #     cv2.waitKey(0)
    # cv2.imshow("Original_Image", img)
    # cv2.imshow("Grayscale", sharp)
    # cv2.imshow("Adaptive", adapt)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()