import cv2
import numpy as np

class smoothing:
    def __init__(self,uploaded_image):
        self.img = uploaded_image


    def clean_noise(self):
        # blur
        blur = cv2.bilateralFilter(img[i].copy(), 9, 75, 75)

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
        cv2.imwrite("images/original/Graph.png", img_result)
        image = cv2.imread('images/original/Graph.png')
        return image

if __name__ == '__main__':
    images = ['download.png', 'draw.jpeg', 'graph.jpeg', 'charts.png', 'google.jpeg', 'barGraph.jpeg']
    img = []
    saturation = []
    bilateralBlur = []
    threshold = []
    # print(img)

    for i in range(len(images)):
        img.append(cv2.imread(images[i]))

    #Applying the blurring algorithms
    for i in range(len(img)):
        bilateralBlur.append(cv2.bilateralFilter(img[i].copy(), 15, 75, 75))

    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    filter = np.array([[0, 0, -1, 0, 0], [0, -1, -2, -1, 0], [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]])
    for i in range(len(img)):
        saturation.append(cv2.filter2D(src=bilateralBlur[i], ddepth=-1, kernel=filter))
        # threshold.append(cv2.filter2D(src=img[i].copy(), ddepth=-1, kernel=kernel))
        # bilateralBlur[i] = cv2.filter2D(img[i].copy(), -1, filter)


    # convert to hsv and get saturation channel
    threshold.clear()
    for i in range(len(saturation)):
        threshold.append(cv2.cvtColor(saturation[i], cv2.COLOR_BGR2HSV))

    # threshold saturation channel
    # for i in range(len(saturation)):
    #     threshold[i] = cv2.threshold(threshold[i], 50, 255, cv2.THRESH_BINARY)[1]

    # apply morphology close and open to make mask
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    # morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    # mask = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel, iterations=1)
    # morph = []
    # mask = []
    # for i in range(len(saturation)):
    #     mask.append(cv2.Canny(saturation[i], 100, 200))
        # obj = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
        # morph.append(cv2.morphologyEx(saturation[i], cv2.MORPH_CLOSE, obj, iterations=1))
        # mask.append(cv2.morphologyEx(morph[i], cv2.MORPH_OPEN, obj, iterations=1))


    for i in range(len(img)):
        cv2.imshow("Original_Image", img[i])
        # cv2.imshow("MexicanHatExlBlur", bilateralBlur[i])
        cv2.imshow("MexicanHatBlur", saturation[i])
        # cv2.imshow("MexicanToHsv", threshold[i])
        # cv2.imshow("Morphology", morph[i])
        # cv2.imshow("Edges", mask[i])
        cv2.waitKey(0)

    cv2.destroyAllWindows()

