import cv2
import numpy as np
# read image
img = cv2.imread('draw.jpeg')

# blur
blur = cv2.medianBlur(img, 5)

# convert to hsv and get saturation channel
sat = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)[:,:,1]

# threshold saturation channel
thresh = cv2.threshold(sat, 50, 255, cv2.THRESH_BINARY)[1]

# apply morphology close and open to make mask
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
mask = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel, iterations=1)

# do OTSU threshold to get circuit image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# write black to otsu image where mask is black
otsu_result = otsu.copy()
otsu_result[mask==0] = 0

# write black to input image where mask is black
img_result = img.copy()
img_result[mask==0] = (255,255,255)

# write result to disk
# cv2.imwrite("images/Graph.png", img_result)
# cv2.imwrite("images/original/circuit_board_mask.png", mask)
# cv2.imwrite("images/original/circuit_board_otsu.png", otsu)
# cv2.imwrite("images/original/circuit_board_otsu_result.png", otsu_result)
# cv2.imwrite("images/original/circuit_board_img_result.png", img_result)


# display it
cv2.imshow("IMAGE", img)
# cv2.imshow("Opening", opening)
# cv2.imshow("MASK", mask)
# cv2.imshow("OTSU", otsu)
# cv2.imshow("OTSU_RESULT", otsu_result)
cv2.imshow("IMAGE_RESULT", img_result)
cv2.imwrite("images/original/Graph.png", img_result)
image = cv2.imread('images/original/Graph.png')
image[np.where((image==[0, 0, 0]).all(axis=2))] = [0, 0, 255]
cv2.imshow("Original to red", image)
cv2.waitKey(0)

# Morphological transformation
# _, mask = cv.threshold(img, 250, 255, cv.THRESH_BINARY_INV)
#
# # Use dilation to fill the holes in mask of the original image
# # the kernel size is directly proportional to the dilation
# kernel = np.ones((5, 5), np.uint8)
# dilation = cv.dilate(mask, kernel)
# erosion = cv.erode(mask, kernel)
# erosion1 = cv.erode(mask, kernel, iterations=3)
#
#
# # Normally, in cases like noise removal, erosion is followed by dilation.
# # Because, erosion removes white noises, but it also shrinks our object.
# # So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
# # It is also useful in joining broken parts of an object.
# # applies dilation first, the erosion
# opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=2)
# # inverse of opening
# closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
#
#
# cv.imshow("Orange GreyScale", img)
# cv.imshow("Mask", mask)
# cv.imshow("Dilation", dilation)
# cv.imshow("Erosion", erosion)
# cv.imshow("Too much Erosion", erosion1)
# cv.imshow("Opening", opening)
# cv.imshow("Closing", closing)
# cv.waitKey(0)
# cv.destroyAllWindows()


# Image smoothing using blur functions
# img = cv.imread("lake.jpeg")
# averaging = cv.blur(img, (21, 21))
# gaussian = cv.GaussianBlur(img, (21, 21), 0)
# # @median works really well when we have noisy image
# median = cv.medianBlur(img, 5)
# # @Arg3...As you increase the sigmoid value(parameter no 3), you get a cartoon effect.
# bilateral = cv.bilateralFilter(img, 9, 350, 350)
#
# cv.imshow("Original image", img)
# # cv.imshow("Averaging", averaging)
# # cv.imshow("Gaussian", gaussian)
# # cv.imshow("Median", median)
# cv.imshow("Bilateral", bilateral)
#
# cv.waitKey(0)
# cv.destroyAllWindows()
