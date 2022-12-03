import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Maths', 'Physics', 'Chemistry', 'Biology', 'English'])
y = np.array([23, 17, 35, 29, 12])

plt.title("Students Enrolled")
plt.xlabel("Subjects")
plt.ylabel("Number of students")

plt.bar(x, y)
plt.show()