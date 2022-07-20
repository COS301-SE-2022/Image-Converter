import cv2
import numpy as np
import glob
import os

logo = cv2.imread("logo/logo-test.png")
print(logo.shape)
scale_percent = 0.25
width = int(logo.shape[1]*scale_percent)
height = int(logo.shape[0]*scale_percent)
dimension = (width, height)

resized = cv2.resize(logo, dimension, interpolation=cv2.INTER_AREA)
print(resized.shape)
print(logo.shape)

# cv2.imwrite('resized_logo.png', resized)
# print(logo)
h_logo, w_logo, _ = resized.shape

images_path = glob.glob("images/*.*")

print("Adding watermark")
for img_path in images_path:
    img = cv2.imread(img_path)
    h_img, w_img, _ = img.shape

    # Get the center of the original. It's the location where we will place the watermark
    center_y = int(h_img / 30)
    center_x = int(w_img / 30)
    top_y = center_y - int(h_logo / 50)
    left_x = center_x - int(w_logo / 50)
    bottom_y = top_y + h_logo
    right_x = left_x + w_logo

    # Get ROI
    roi = img[top_y: bottom_y, left_x: right_x]

    # Add the Logo to the Roi
    # result = cv2.addWeighted(roi, 1, logo, 1, 0)

    # Replace the ROI on the image
    img[top_y: bottom_y, left_x: right_x] = resized

    # Get filename and save the image
    filename = os.path.basename(img_path)
    cv2.imwrite("images/watermarked_" + filename, img)


print("Watermark added to all the images")