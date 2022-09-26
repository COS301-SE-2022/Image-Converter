import cv2
import numpy as np
from converter.watermark import AddMark
from converter.resizing import imageResizing
from PIL import Image
import sys
sys.path.append('../')

class smoothing:
    def __init__(self,uploaded_image):
        self.img = uploaded_image

    def clean_noise(self):
        import time
        start = time.time()
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        # Read the desired model
        path = "converter/RealESRGAN_x4plus.pth"
        sr.readModel(path)
        sr.setModel("edsr",4)

        # Set CUDA backend and target to enable GPU inference
        sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        
        result = sr.upsample(self.img)
        end = time.time()
        print(end - start)

        # sr = cv2.dnn_superres.DnnSuperResImpl_create()
        # path = "ESPCN_x4.pb"
        # print('------------------------Loading model1----------------------------------------')
        # sr.readModel(path)
        # sr.setModel("espcn",4)
        # result = sr.upsample(self.img)
        # print('------------------------DONE Loading model-------------------------------------')


        # sr1 = cv2.dnn_superres.DnnSuperResImpl_create()
        # path = "EDSR_x4.pb"
        # print('------------------------Loading model 2----------------------------------------')
        # start = time.time()
        # sr1.readModel(path)
        # sr1.setModel("edsr",4)
        # result1 = sr1.upsample(self.img)
        # end = time.time()
        # print(end - start)
        # print('------------------------DONE Loading model----------------------------------------')
        
        # sr2 = cv2.dnn_superres.DnnSuperResImpl_create()
        # path = "LapSRN_x8.pb"
        # print('------------------------Loading model3----------------------------------------')
        # sr2.readModel(path)
        # sr2.setModel("lapsrn",8)
        # result2 = sr2.upsample(self.img)
        # print('------------------------DONE Loading model----------------------------------------')

        # kernel = np.array([[0, -1, 0],
        #            [-1, 5,-1],
        #            [0, -1, 0]])

        # # kernel = np.ones((5, 5), np.float32)/30
        # image_sharp = cv2.filter2D(src=self.img, ddepth=-1, kernel=kernel)
        # #Image smoothing and sharpening
        # blurred = cv2.bilateralFilter(self.img, 15, 75, 75)
        # sharp = cv2.addWeighted(self.img, 3.5, self.img, -2.1, 0)
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # open = cv2.morphologyEx(sharp, cv2.MORPH_OPEN, kernel, iterations=1)

        # Using cv2.imshow() method 
        # Displaying the image 
        cv2.imshow("Original Image", self.img)
        cv2.imshow("ESDSR_x4", result)
        # cv2.imshow("eDsr_x4", result1)
        # cv2.imshow("LapSRN_x8", result2)
        
        # waits for user to press any key 
        # (this is necessary to avoid Python kernel form crashing)
        cv2.waitKey(0) 
        
        # closing all open windows 
        cv2.destroyAllWindows() 

        #Resizing the image
        resizedImage = imageResizing(result)
        resizedImage = resizedImage.resize()
        print('Resized image:', resizedImage.shape)

        #Adding a watermark to the image
        imageWatermark = AddMark(Image.fromarray(cv2.cvtColor(resizedImage, cv2.COLOR_BGR2RGB)))
        imageWatermark = imageWatermark.Dev()

        # #Converting the returned image to numpy array
        cleanedImage = np.array(imageWatermark) 
        cleanedImage = cleanedImage[:, :, ::-1].copy() 


        cv2.imwrite("./../images/original/Graph.png", cleanedImage)
        return cleanedImage

if __name__ == '__main__':
    src = [ '/Users/neoseefane/Documents/GitHub/Image-Converter/Server/converter/graphs/imagemg8c19s191e1pa1p2answer.png']
    for i in src:
        img = cv2.imread(i)
        object = smoothing(img)
        object.clean_noise()
    