from converter.smoothing import smoothing
import cv2 as cv


def test_smoothing():
    image = cv.imread('draw.jpeg')
    object = smoothing(image)
    originalImage = object.clean_noise()
    duplicateImage = cv.imread('images/original/Graph.png')
    difference = cv.subtract(originalImage, duplicateImage)
    black, green, red = cv.split(difference)

    assert originalImage.shape == duplicateImage.shape
    assert cv.countNonZero(red) == 0
    assert cv.countNonZero(green) == 0
    assert cv.countNonZero(black) == 0


