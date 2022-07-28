from PIL import Image
import sys
sys.path.append('../')

class AddMark:

    def __init__ (self,uploaded_image):
        self.img = uploaded_image

    def Dev(self):
        # Getting the height and width of the image
        width, height = self.img.size

        size = (100, 100)
        logo = Image.open(r'./logo/logo-test.png', 'r')

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