import numpy as np
import matplotlib.pyplot as plt

# dev_x = [25, 26,27, 28]
# dev_y = [1000, 2000, 3000, 4000]

# plt.plot(dev_x, dev_y)

# plt.xlabel('ages')
# plt.ylabel('salary')
# plt.title('salary by age')
# print('show')
# plt.show()
# print('done')

x = np.arange(-100, 100, 1)
y = 0.5*x**2 + 2*x
plt.plot(x,y)
plt.show()
print('done')