from PIL import Image


class AddMark:

    def __init__(self, uploaded_image):
        self.img = uploaded_image

    def Dev(self):
       
        # Get height and width of the image
        width, height = self.img.size

        size = (100, 100)
        # print(size)
        # print(self.img.size)

        logo = Image.open('logo/logo-test.png') #set logo to desired watermark in folder

        logo.thumbnail(size)

        # Location where we want to paste watermark on the uploaded image
        x = width - 100 - 10
        y = height - 100 - 0

        self.img.paste(logo, (x, y)) #paste watermark to original image
        # Save the image to results folder
        self.img.save('results/image_with_logo.jpg')

        # Opening the new image
        img = Image.open('results/image_with_logo.jpg')
        img.show()
        print("done")
        return self.img #return final image 


if __name__ == '__main__':
    obj = AddMark(Image.open('images/bar3.jpg')) # create object

    obj.Dev() # call Dev function on object

# import cv2
# import numpy as np
# import glob
# import os


# class AddMark:

#     def Dev():
#         mark = cv2.imread("logo/logo-test.png")
#         # print(mark.shape)
#         scale_percent = 0.25
#         width = int(mark.shape[1]*scale_percent)
#         height = int(mark.shape[0]*scale_percent)
#         dimension = (width, height)

#         resized = cv2.resize(mark, dimension, interpolation=cv2.INTER_AREA)
#         # print(resized.shape)
#         # print(mark.shape)

#         # cv2.imwrite('resized_logo.png', resized)
#         # print(logo)
#         h_logo, w_logo, _ = resized.shape

#         images_path = glob.glob("images/*.*")

#         print("Adding watermark")
#         for img_path in images_path:
#             img = cv2.imread(img_path)
#             h_img, w_img, _ = img.shape

#             # Get the center of the original. It's the location where we will place the watermark
#             center_y = int(h_img / 30)
#             center_x = int(w_img / 30)
#             top_y = center_y - int(h_logo / 50)
#             left_x = center_x - int(w_logo / 50)
#             bottom_y = top_y + h_logo
#             right_x = left_x + w_logo

#             # Get ROI
#             roi = img[top_y: bottom_y, left_x: right_x]

#             # Add the Logo to the Roi
#             # result = cv2.addWeighted(roi, 1, logo, 1, 0)

#             # Replace the ROI on the image
#             img[top_y: bottom_y, left_x: right_x] = resized

#             # Get filename and save the image
#             filename = os.path.basename(img_path)
#             # cv2.imwrite("images/watermarked_" + filename, img)
#             cv2.imwrite('results/watermarked_' + filename, img)

#         print("Watermark added to all the images")
