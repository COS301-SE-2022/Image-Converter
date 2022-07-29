from converter.graphPloting import GraphPloting
import cv2
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from pathlib import Path

def test_formated_formula():
    #Prepare data
    object = GraphPloting()

    #Act
    object.draw('5*x')

    #Assert
    assert object.formatedFormula == '5x'

def test_returned_image():
    #Prepare data
    object = GraphPloting()
    workingDir = Path(__file__).parent  
    filePath = workingDir / 'images/plottedGraph.png' 

    #Act
    drawing = object.draw('5*x')
    returnedImage = cv2.imread(str(filePath))

    #Assert
    assert drawing == returnedImage
