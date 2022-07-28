from converter.resizing import imageResizing
import cv2
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

def testImageSizeBeforeResizing():
    #Prepare data
    object = imageResizing(cv2.imread('./../draw.jpeg'))
   
    #Assert
    assert object.resizedImage.shape == (3027, 3104, 3)

def testImageSizeBeforeAndAfterResizing():
    #Prepare data
    object = imageResizing(cv2.imread('./../draw.jpeg'))
    
    #Assert
    assert object.resizedImage.shape == (3027, 3104, 3)
    object.resize()
    assert object.resizedImage.shape == (800, 800, 3)