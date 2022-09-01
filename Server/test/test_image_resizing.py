from converter.resizing import imageResizing
import cv2
import os


def testImageSizeBeforeResizing():
    #Prepare data
    filePath = os.path.join(os.getcwd() + r'\draw.jpeg' )
    #Act
    object = imageResizing(cv2.imread(str(filePath)))

    #Assert
    assert object.resizedImage.shape == (3027, 3104, 3)

def testImageSizeBeforeAndAfterResizing():
    #Prepare data
    filePath = os.path.join(os.getcwd() + r'\draw.jpeg' )

    #Act
    object = imageResizing(cv2.imread(str(filePath)))
    
    #Assert
    assert object.resizedImage.shape == (3027, 3104, 3)
    object.resize()
    assert object.resizedImage.shape == (800, 800, 3)