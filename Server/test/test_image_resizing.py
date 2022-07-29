from converter.resizing import imageResizing
import cv2
from pathlib import Path
import os


def testImageSizeBeforeResizing():
    #Prepare data
    workingDir = Path(__file__).parent  
    filePath = workingDir / 'draw.jpeg'  
    os.chdir(str(filePath))

    #Act
    object = imageResizing(cv2.imread(str(filePath)))

    #Assert
    print(object.resizedImage)
    assert object.resizedImage.shape == (3027, 3104, 3)

# def testImageSizeBeforeAndAfterResizing():
#     #Prepare data
#     workingDir = Path(__file__).parent  
#     filePath = workingDir / 'draw.jpeg' 

#     #Act
#     object = imageResizing(cv2.imread(str(filePath)))
    
#     #Assert
#     assert object.resizedImage.shape == (3027, 3104, 3)
#     object.resize()
#     assert object.resizedImage.shape == (800, 800, 3)