import matplotlib.pyplot as plt
import numpy as np


Sleeping = [6, 7, 5, 8, 6] 
Eating = [2, 2, 1, 2, 1]
Studying = [5, 7, 10, 8, 6] 
Playing = [3, 3, 0, 1, 3] 
y = np.vstack([Sleeping, Eating, Studying, Playing])
x = np.array([ 1, 2, 3, 4, 5])
c = np.array(['g', 'b', 'r', 'c'])
n = np.array(["system 1", "system 2", "system 3", "system 4"])


plt.stackplot(x, y, colors=c, labels=n)
plt.legend(loc='upper left')
plt.show()

