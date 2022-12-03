import matplotlib.pyplot as plt
import numpy as np

y1 =  np.array([65, 80, 98, 76, 85])
y2 =  np.array([80, 70, 60, 90, 95])
x =  np.array([100, 200, 300, 400, 500]) 

plt.title("Comparison of Accuracy of system 1 and 2")
plt.xlabel("Input size")
plt.ylabel("Accuracy percentage")

plt.bar(x-10, y1, color='g', width=20)
plt.bar(x+10, y2, width=20)
plt.legend(["system 1", "system 2"])
# The barh() takes the keyword argument height to set the height of the bars:
plt.show()