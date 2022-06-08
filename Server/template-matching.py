import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

graphType = ""
# Line Graph
# img1 = cv.imread('assets/line-graph-copy.jpg',cv.IMREAD_GRAYSCALE)          # queryImage
# img1 = cv.imread('assets/line-graph2.webp',cv.IMREAD_GRAYSCALE)          # queryImage

# Bar Graph
# img1 = cv.imread('assets/bargraph.png',cv.IMREAD_GRAYSCALE)          # queryImage
img1 = cv.imread('assets/barchart.jpg',cv.IMREAD_GRAYSCALE)          # queryImage

# Pie Chart
# img1 = cv.imread('assets/piechart1.jpg',cv.IMREAD_GRAYSCALE)          # queryImage

# Parabola
# img1 = cv.imread('assets/parabola1.jpg',cv.IMREAD_GRAYSCALE)          # queryImage


def line_graph():
    # img1 = cv.imread('assets/line-graph-copy.jpg',cv.IMREAD_GRAYSCALE)          # queryImage
    img2 = cv.imread('assets/line-graph-copy.jpg',cv.IMREAD_GRAYSCALE) # trainImage
    # # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    goodMatches = 0
    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]


    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            goodMatches+=1 
            matchesMask[i]=[1,0]
    draw_params = dict(matchColor = (0,255,0),
                    singlePointColor = (255,0,0),
                    matchesMask = matchesMask,
                    flags = cv.DrawMatchesFlags_DEFAULT)
    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    print("Linegraph")
    print("Number of Matches: ",goodMatches)
    print()

    if(goodMatches > 5 ):
        graphType = "linegraph"
        # print(graphType)


    # plt.imshow(img3),plt.show()

def barchart():
    # img1 = cv.imread('assets/bargraph.png',cv.IMREAD_GRAYSCALE)          # queryImage
    img2 = cv.imread('assets/barchart-template.jpg',cv.IMREAD_GRAYSCALE) # trainImage
    # # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    goodMatches = 0
    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]


    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            goodMatches+=1 
            matchesMask[i]=[1,0]
    draw_params = dict(matchColor = (0,255,0),
                    singlePointColor = (255,0,0),
                    matchesMask = matchesMask,
                    flags = cv.DrawMatchesFlags_DEFAULT)
    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    print("Barchart")
    print("Number of Matches: ",goodMatches)
    print()

    if(goodMatches > 5 ):
        graphType = "barchart"

    # plt.imshow(img3),plt.show()


def pie_chart():
    img2 = cv.imread('assets/piechart-template.jpg',cv.IMREAD_GRAYSCALE) # trainImage
    # # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    goodMatches = 0
    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]


    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            goodMatches+=1 
            matchesMask[i]=[1,0]
    draw_params = dict(matchColor = (0,255,0),
                    singlePointColor = (255,0,0),
                    matchesMask = matchesMask,
                    flags = cv.DrawMatchesFlags_DEFAULT)
    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    print("Piechart")
    print("Number of Matches: ",goodMatches)
    print()

    if(goodMatches > 5 ):
        graphType = "piechart"
        # print(graphType)


    # plt.imshow(img3),plt.show()

def parabola():
    img2 = cv.imread('assets/parabola-template-resized.png',cv.IMREAD_GRAYSCALE) # trainImage
    # # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    goodMatches = 0
    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]


    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            goodMatches+=1 
            matchesMask[i]=[1,0]
    draw_params = dict(matchColor = (0,255,0),
                    singlePointColor = (255,0,0),
                    matchesMask = matchesMask,
                    flags = cv.DrawMatchesFlags_DEFAULT)
    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    print("Parabola")
    print("Number of Matches: ",goodMatches)
    print()

    if(goodMatches > 5 ):
        graphType = "parabola"
        # print(graphType)


    # plt.imshow(img3),plt.show()



if __name__ == "__main__": 

    line_graph()
    barchart()
    pie_chart()
    parabola()