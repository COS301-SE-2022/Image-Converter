# from converter.templateMatching import Matching
# import numpy as np
# import cv2 as cv


# def test_TemplateMatching_GivenASmoothedImage_ShouldReturnMatchPercentage():
#     #Prepare
#     image = cv.imread('assets/line-graph.jpg')

#     #Act
#     object = Matching(image)
#     lineGraph = object.line_graph()
#     pieChart = object.pie_chart()
#     barChart = object.barchart()
#     scatterPlot = object.scatterplot()

#     #Assert
#     assert lineGraph == 102
#     assert pieChart == 0
#     assert barChart == 6
#     assert scatterPlot == 17

