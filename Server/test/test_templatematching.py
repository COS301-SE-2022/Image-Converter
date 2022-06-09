from converter.templateMatching import Matching
import numpy as np
import cv2 as cv


def test_template():
    image = cv.imread('assets/line-graph.jpg')
    object = Matching(image)
    tempImg = object.line_graph()
    assert tempImg == 50
    tempImg = object.pie_chart()
    assert tempImg == 50
