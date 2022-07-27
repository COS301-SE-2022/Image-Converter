
import numpy as np
import matplotlib.pyplot as plt

xAxisLabel = input("Enter x axis label")
yAxisLabel = input("Enter y axis label")
titleLabel = input("Enter title")
 
first_label = input("Enter first label ")
first_label_value = int(input("Enter first number "))

second_label = input("Enter second label")
second_label_value = int(input("Enter second number "))

# third_label = input("Enter third label ")
# third_label_value = int(input("Enter third number "))

# fourth_label = input("Enter fourth label ")
# fourth_label_value = int(input("Enter fourth number "))


data = {first_label:first_label_value, second_label:second_label_value, 
# third_label:third_label_value,
#         fourth_label:fourth_label_value
        }
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))


plt.bar(courses, values, color ='black',
        width = 0.4)
 
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)
plt.title(titleLabel)
plt.savefig("bargraph.png", bbox_inches="tight", pad_inches=2)
plt.show()



