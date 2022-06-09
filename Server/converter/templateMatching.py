import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

class Matching:
    def __init__(self,uploaded_image):
        self.uploaded_image = uploaded_image
        self.perfectMatch = 0
        self.graphType = ""
        self.match()


    def match(self):
        print(self.line_graph())
        print(self.barchart())
        # print(self.pie_chart())
        print(self.scatterplot())

    def line_graph(self):
        img2 = cv.imread('assets/line-graph-copy.jpg',cv.IMREAD_GRAYSCALE)

        sift = cv.SIFT_create()
        keypts1, desc1 = sift.detectAndCompute(self.uploaded_image,None)
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

        if(goodMatches > self.perfectMatch):
            self.perfectMatch = goodMatches
            self.graphType = "Line Graph"
        return goodMatches

    def barchart(self):
        img2 = cv.imread('assets/barchart-template.jpg',cv.IMREAD_GRAYSCALE) 

        sift = cv.SIFT_create()

        keypts1, desc1 = sift.detectAndCompute(self.uploaded_image,None)
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

        if(goodMatches > self.perfectMatch):
            self.perfectMatch = goodMatches
            self.graphType = "Bar Graph"
        return goodMatches


    def pie_chart(self):
        img2 = cv.imread('assets/piechart-template.jpg',cv.IMREAD_GRAYSCALE) 

        sift = cv.SIFT_create()

        keypts1, desc1 = sift.detectAndCompute(self.uploaded_image,None)
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

        if(goodMatches > self.perfectMatch):
            self.perfectMatch = goodMatches
            self.graphType = "Pie Chart"
        return goodMatches


    def scatterplot(self):
        img2 = cv.imread('assets/scatterplot-template.png',cv.IMREAD_GRAYSCALE) 
    
        sift = cv.SIFT_create()

        keypts1, desc1 = sift.detectAndCompute(self.uploaded_image,None)
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

        if(goodMatches > self.perfectMatch):
            self.perfectMatch = goodMatches
            self.graphType = "Scatterplot"
        return goodMatches
