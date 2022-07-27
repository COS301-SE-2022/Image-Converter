# Import libraries
from matplotlib import pyplot as plt
import numpy as np
 
# xAxisLabel = input("Enter x axis label")
# yAxisLabel = input("Enter y axis label")
# titleLabel = input("Enter title")
 
first_label = input("Enter first label ")
first_label_value = int(input("Enter first number "))

second_label = input("Enter second label")
second_label_value = int(input("Enter second number "))

third_label = input("Enter third label")
third_label_value = int(input("Enter second number "))

# cars = ['AUDI', 'BMW', 'FORD',
#         'TESLA', 'JAGUAR', 'MERCEDES']

labels_array = [first_label, second_label, third_label]
 
data = [first_label_value, second_label_value, third_label_value]

# plt.xlabel(xAxisLabel)
# plt.ylabel(yAxisLabel)
# plt.title(titleLabel)
 
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = labels_array)
 
plt.savefig("piegraph.png", bbox_inches="tight", pad_inches=2)
plt.show()