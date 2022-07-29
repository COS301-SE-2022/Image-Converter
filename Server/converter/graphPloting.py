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
    def __init__(self):
        self.formatedFormula = ""
        self.pos = 0
        self.divisionFlag = False
        self.denominator = "" 

    def draw(self, formula):
        #generating the x and y
        x = np.linspace(-np.pi, np.pi, 100)
        y = eval(formula)

        # use set_position
        axis = plt.gca()
        axis.spines['top'].set_color('none')
        axis.spines['left'].set_position('zero')
        axis.spines['right'].set_color('none')
        axis.spines['bottom'].set_position('zero')

        latex = [r'$\dfrac{a}{b}$', r'$a^a$',]
        for i in range(len(formula)):
            if(formula[i] == '*'):
                self.formatedFormula += ''
            else:
                 self.formatedFormula += formula[i]

        #plotting the graph
        plt.plot(x, y, '-r', label=formula)
        # print(r'$\frac{a}{b}$')
        plt.title('Graph of ' + formula)
        plt.grid()
        # print("hello")
        # print('Test', str(filePath)) 
        plt.savefig('./../images/plottedGraph.png')
        # print("hello2")
        # plt.show()
        plt.close

        # plottedImage = cv2.imread('images/plottedGraph.png')
        #Resizing the image
        # print("Olo", str(filePath))
        plottedImage = cv2.imread('./../images/plottedGraph.png')
        resizedImage = imageResizing(plottedImage)
        resizedImage = resizedImage.resize()
        # print('Resized image:', resizedImage.shape)

        #Adding a watermark to the image
        imageWatermark = AddMark(Image.fromarray(cv2.cvtColor(resizedImage, cv2.COLOR_BGR2RGB)))
        imageWatermark = imageWatermark.Dev()

        #Converting the returned image to numpy array
        finalDrawing = np.array(imageWatermark) 
        finalDrawing = finalDrawing[:, :, ::-1].copy() 
        # print("Image: ", finalDrawing.shape)

        cv2.imwrite("./../images/plottedGraph.png", finalDrawing)
        # print(finalDrawing)

        return finalDrawing


    
if __name__ == '__main__':
    input = ['(x**2)+2*x+2', '5*x', '5**x', '5/x-11']
    draw = GraphPloting()
    draw.draw(input[1])
    
    # for i in range(len(input)): 
    #     draw.draw(input[i])
    # draw.parabola(input[0])