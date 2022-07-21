from PIL import Image

class imageResizing:
    def __init__(self, image):        
        self.resizedImage = image

    def resize(self):
        self.resizedImage = self.resizedImage.resize((800,800))
        return self.resizedImage

if __name__ == '__main__':
    obj = imageResizing(Image.open('draw.jpeg'))
    resizedImage = obj.resize()
    print(resizedImage.size)