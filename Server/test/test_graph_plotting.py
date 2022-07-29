from converter.graphPloting import GraphPloting
import cv2
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

def test_formated_formula():
    #Prepare data
    object = GraphPloting()
    
    # print('sssss', os.listdir(r'.\..\converter\logo'))
    #Act
    object.draw('5*x')

    print(os.getcwd)
    #Assert
    assert object.formatedFormula == '5x'

def test_returned_image():
    #Prepare data
    object = GraphPloting()

    #Act
    drawing = object.draw('5*x')
    returnedImage = cv2.imread('images/plottedGraph.png')

    #Assert
    assert drawing == returnedImage
