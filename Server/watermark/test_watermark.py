import unittest
import os
from watermark import AddMark
from PIL import Image

# class TestWatermark(unittest.TestCase):

def test_watermark():
    testImg = Image.open('images/bar3.jpg')
    testLogo = Image.open('logo/logo-test.png')

    if os.path.exists('images/bar3.jpg') and os.path.exists('logo/logo-test.png'):

        width, height = testImg.size

        size = (100, 100)

        testLogo.thumbnail(size)

        
        # Location where we want to paste watermark on the uploaded image
        x = width - 100 - 10
        y = height - 100 - 0

        testImg.size.paste(testLogo, (x, y))

        assert os.path.exists('images/bar3.jpg') == True
        assert os.path.exists('logo/logo-test.png') == False

    if os.path.exists('saveTestImg'):
        testImg.save('saveTestImg/testImg_with_logo.jpg')
        assert os.path.exists('saveTestImg') == True

    else:
        assert os.path.exists('saveTestImg') == False


if __name__ == '__main__':
    unittest.main()
