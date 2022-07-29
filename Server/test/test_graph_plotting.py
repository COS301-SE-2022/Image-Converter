from converter.graphPloting import GraphPloting
import pytest
import cv2
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

@pytest.mark.xfail(reason="The image path cannot be read, as such the test fails")
def test_formated_formula():
    #Prepare data
    object = GraphPloting()

    #Act
    object.draw('5*x')

    #Assert
    assert object.formatedFormula == '5x'

@pytest.mark.xfail(reason="The image path cannot be read, as such the returned image is null")
def test_returned_image():
    #Prepare data
    object = GraphPloting()

    #Act
    drawing = object.draw('5*x')
    returnedImage = cv2.imread('./../images/plottedGraph.png')

    #Assert
    assert drawing == returnedImage
