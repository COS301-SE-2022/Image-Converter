import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models

(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load.data()
training_images = training_images/255
testing_images = testing_images/255

class_graphs = ['Bargraph', 'ScatterPlot,', 'LineGraph', 'PieChart']

for i in range(16):
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(training_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_graphs[training_labels[i][0]])

    plt.show()


