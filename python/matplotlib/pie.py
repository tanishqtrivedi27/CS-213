import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

# The startangle parameter is defined with an angle in degrees, default angle is 0:
# plt.pie(y, labels = mylabels, startangle = 90)

# explode
# myexplode = [0.2, 0, 0, 0]

# plt.pie(y, labels = mylabels, explode = myexplode)

# shadwos
# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)

# colors=mycolors

# plt.legend(title = "Four Fruits:")

# histogram
# plt.hist()