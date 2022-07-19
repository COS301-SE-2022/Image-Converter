from image_resizing.resizing import imageResizing
from PIL import Image


def testImageSizeBeforeResizing():
    #prepare
    object = imageResizing(Image.open('draw.jpeg'))

    #act
    assert object.resizedImage.size == (3104, 3027)

def testImageSizeBeforeAndAfterResizing():
    #prepare
    object = imageResizing(Image.open('draw.jpeg'))

    #act
    assert object.resizedImage.size == (3104, 3027)
    object.resize()
    assert object.resizedImage.size == (500, 500)