from PIL import Image
import cv2

class imageResizing:
    def __init__(self, image):        
        self.resizedImage = image

    def resize(self):
        dimension = (800, 800)
        self.resizedImage = cv2.resize(self.resizedImage, dimension, interpolation=cv2.INTER_AREA)
        return self.resizedImage

if __name__ == '__main__':
    obj = imageResizing(cv2.imread('barGraph.jpeg'))
    resizedImage = obj.resize()
    print(resizedImage.shape)