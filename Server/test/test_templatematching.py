from templateMatching import Matching

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def test_template():
    image = cv.imread('assets/linegraph.jpg')
    object = Matching(image)
    tempImg = object.line_graph()
    assert tempImg == 50

    tempImg = object.pie_chart()
    assert tempImg == 50


# from converter.template-matching import template-matching
# import cv2 as cv

# def test_template():
#     image = cv.imread('draw.jpeg')
#     object = Matching(image)
#     originalImage = object.clean_noise()
#     duplicateImage = cv.imread('images/original/Graph.png')
#     difference = cv.subtract(originalImage, duplicateImage)
#     black, green, red = cv.split(difference)

#     assert originalImage.shape == duplicateImage.shape
#     assert cv.countNonZero(red) == 0
#     assert cv.countNonZero(green) == 0
#     assert cv.countNonZero(black) == 0
