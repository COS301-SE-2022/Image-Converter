import numpy as np
import cv2

# img = cv2.resize(cv2.imread('assets/barchart.jpg', 0), (0, 0), fx=0.6, fy=0.6)        #grayscale images
# img = cv2.resize(cv2.imread('assets/line-graph.jpg', 0), (0, 0), fx=0.6, fy=0.6) 
img = cv2.resize(cv2.imread('../assets/line-graph.jpg', 0), (0, 0), fx=0.6, fy=0.6)
template = cv2.resize(cv2.imread('../assets/line-graph-copy.jpg', 0), (0, 0), fx=0.6, fy=0.6)

# img = cv2.imread('assets/download.png', 0)       #grayscale images
# template = cv2.imread('assets/line-graph-copy.jpg', 0)

h, w = template.shape   #tuple (height, width)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] #Different methods for doing TM. Uses all the methods for TM

for method in methods:
    img2 = img.copy()       #Copying the image to draw the rectangle. New image for each method

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img2, location, bottom_right, (0,0,0), 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()