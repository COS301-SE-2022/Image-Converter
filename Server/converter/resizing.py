from PIL import Image
import cv2

class imageResizing:
    def __init__(self, image):        
        self.resizedImage = image

    def resize(self):
        # down_points = (800, 800)
        # cv2.resize(self.resizedImage, down_points, cv2.INTER_LINEAR)
        self.resizedImage = self.resizedImage.resize((800,800))
        return self.resizedImage

if __name__ == '__main__':
    obj = imageResizing(Image.open('draw.jpeg'))
    resizedImage = obj.resize()
    print(resizedImage.size)