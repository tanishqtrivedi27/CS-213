import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([5, 8, 10])
x2 = np.array([6, 9, 11] )
y1 = np.array([12, 16, 6] )
y2 = np.array([6, 15, 7] )

plt.title("XY- plotting")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")

plt.plot(x1, y1, c='g', marker='o', lw=5)
plt.plot(x2, y2, c='c', marker='*', lw=2)
plt.show()