import matplotlib.pyplot as plt
import numpy as np

x = np.array([6.1, 5.8, 5.7, 5.7, 5.8, 5.6, 5.5, 5.3, 5.2, 5.2])
y = np.array([1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565])

plt.title("u vs s")
plt.xlabel("u")
plt.ylabel("s")

plt.scatter(x, y, color = 'g')
plt.grid()
# You can use the axis parameter in the grid() function to specify which grid lines to display.

# Legal values are: 'x', 'y', and 'both'. Default value is 'both'.
plt.show()

# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

# // colors
# # colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

# # plt.scatter(x, y, c=colors)

# //alpha 
# plt.scatter(x, y, s=sizes, alpha=0.5)

# //sizes
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# plt.scatter(x, y, s=sizes)

# // colormap
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

# plt.scatter(x, y, c=colors, cmap='viridis')