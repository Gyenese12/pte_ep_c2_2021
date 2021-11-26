import  matplotlib.pyplot as plt
import numpy as np

number_on_points = 100
x = np.random.randint(0,500,number_on_points)
y = x + 30 *np.random.rand(number_on_points)
sizes = np.random.randint(0,200,number_on_points)
colors = np.random.randint(0,10,number_on_points)
plt.scatter(x,y, s = sizes,c = colors)
plt.show()
