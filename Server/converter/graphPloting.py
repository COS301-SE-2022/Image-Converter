import matplotlib.pyplot as plt
import numpy as np
from converter.resizing import imageResizing
from converter.watermark import AddMark
import cv2
from PIL import Image
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

class GraphPloting:
    def draw(self, formula):
        x = np.linspace(-10,10,1000)
        y = eval(formula)
        # int(re.search(r'\d+', string1).group())
        plt.plot(x, y, '-r', label=formula)
        plt.title('Graph of ' + formula)
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        # plt.legend(loc='upper left')
        plt.grid()
        print("hello")
        plt.savefig('images/plottedGraph.png')
        print("hello2")
        plt.show()
        plt.close

        plottedImage = cv2.imread('images/plottedGraph.png')
        #Resizing the image
        resizedImage = imageResizing(plottedImage)
        resizedImage = resizedImage.resize()
        print('Resized image:', resizedImage.shape)

        #Adding a watermark to the image
        imageWatermark = AddMark(Image.fromarray(cv2.cvtColor(resizedImage, cv2.COLOR_BGR2RGB)))
        imageWatermark = imageWatermark.Dev()

        #Converting the returned image to numpy array
        finalDrawing = np.array(imageWatermark) 
        finalDrawing = finalDrawing[:, :, ::-1].copy() 
        print("Image: ", finalDrawing.shape)

        cv2.imwrite("./../images/plottedGraph.png", finalDrawing)
        return finalDrawing
    
if __name__ == '__main__':
    input = ['x**2+2*x+2', '5*x', '5**x', '5/x-11']
    draw = GraphPloting()
    draw.draw(input[0])
    
    # for i in range(len(input)): 
    #     draw.draw(input[i])
    # draw.parabola(input[0])