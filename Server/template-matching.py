import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

graphType = ""
# Line Graph
# img1 = cv.imread('assets/line-graph.jpg',cv.IMREAD_GRAYSCALE)          # queryImage
# img1 = cv.imread('assets/line-graph2.webp',cv.IMREAD_GRAYSCALE)          # queryImage

# Bar Graph
# img1 = cv.imread('assets/bargraph.png',cv.IMREAD_GRAYSCALE)          # queryImage
# img1 = cv.imread('assets/barchart.jpg',cv.IMREAD_GRAYSCALE)          # queryImage

# Pie Chart
# img1 = cv.imread('assets/piechart1.jpg',cv.IMREAD_GRAYSCALE)          # queryImage


# Scatterplot
img1 = cv.imread('assets/scatterplot1.webp',cv.IMREAD_GRAYSCALE)          # queryImage



def line_graph():
    img2 = cv.imread('assets/line-graph-copy.jpg',cv.IMREAD_GRAYSCALE)

    sift = cv.SIFT_create()
    keypts1, desc1 = sift.detectAndCompute(img1,None)
    keypts2, desc2 = sift.detectAndCompute(img2,None)

   
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(desc1,desc2,k=2)

    goodMatches = 0

    matchesMask = [[0,0] for i in range(len(matches))]


    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            goodMatches+=1 
            matchesMask[i]=[1,0]


    if(goodMatches > 5 ):
        graphType="linegraph"
        print("Graph is a "+ graphType)


def barchart():
    img2 = cv.imread('assets/barchart-template.jpg',cv.IMREAD_GRAYSCALE) 

    sift = cv.SIFT_create()

    keypts1, desc1 = sift.detectAndCompute(img1,None)
    keypts2, desc2 = sift.detectAndCompute(img2,None)


    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(desc1,desc2,k=2)

    goodMatches = 0
    matchesMask = [[0,0] for i in range(len(matches))]


    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            goodMatches+=1 
            matchesMask[i]=[1,0]


    if(goodMatches > 5 ):
        graphType = "barchart"
        print("Graph is a "+ graphType)



def pie_chart():
    img2 = cv.imread('assets/piechart-template.jpg',cv.IMREAD_GRAYSCALE) 

    sift = cv.SIFT_create()

    keypts1, desc1 = sift.detectAndCompute(img1,None)
    keypts2, desc2 = sift.detectAndCompute(img2,None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(desc1,desc2,k=2)

    goodMatches = 0

    matchesMask = [[0,0] for i in range(len(matches))]


    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            goodMatches+=1 
            matchesMask[i]=[1,0]

 

    if(goodMatches > 5 ):
        graphType = "piechart"
        print("Graph is a "+ graphType)


def scatterplot():
    img2 = cv.imread('assets/scatterplot-template.png',cv.IMREAD_GRAYSCALE) 

    sift = cv.SIFT_create()

    keypts1, desc1 = sift.detectAndCompute(img1,None)
    keypts2, desc2 = sift.detectAndCompute(img2,None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(desc1,desc2,k=2)

    goodMatches = 0

    matchesMask = [[0,0] for i in range(len(matches))]


    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            goodMatches+=1 
            matchesMask[i]=[1,0]


    if(goodMatches > 5 ):
        graphType = "scatterplot"
        print("Graph is a "+ graphType)




if __name__ == "__main__": 

    line_graph()
    barchart()
    pie_chart()
    scatterplot()
