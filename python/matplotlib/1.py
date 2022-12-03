import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,4,5,3])
y = np.array([4,5,11,10,1])

# data = np.array([
#     [1, 4],
#     [2, 5],
#     [4, 11],
#     [5, 10],
#     [3, 1]
# ])
# # Taking transpose
# x, y = data.T

plt.title("XY- plotting")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.plot(x, y, marker = 'o', ms=10, mec='r', mfc = 'b', ls = 'dotted', c='y', lw=5)
#marker type , marker size, marker edge color, marker face color(inside), linestyle, linecolor, linewidth

plt.show()

# marker|line|color
# plt.plot(x, y, '*--r')