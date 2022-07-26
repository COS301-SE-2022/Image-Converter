
import numpy as np
import matplotlib.pyplot as plt

xAxisLabel = input("Enter x axis label")
yAxisLabel = input("Enter y axis label")
titleLabel = input("Enter title")
 
first_label_value = int(input("Enter first number "))
first_label = input("Enter first number ")
second_label_value = int(input("Enter second number "))
third_label_value = int(input("Enter third number "))
fourth_label_value = int(input("Enter fourth number "))


# creating the dataset
data = {first_label:first_label, 'C++':second_label_value, 'Java':third_label_value,
        'Python':fourth_label_value}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='black',
        width = 0.4)
 
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)
plt.title(titleLabel)
plt.show()



