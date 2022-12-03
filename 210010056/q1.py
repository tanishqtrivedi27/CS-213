import numpy as np
import matplotlib.pyplot as plt
import csv

f = open(r'COVID dataset.txt', 'r')

with f:
    reader = csv.reader(f)
    n1 = np.array(next(reader))
    n2 = np.array(next(reader))
    data_2d = np.vstack((n1, n2))
    for row in reader:
        data_2d = np.vstack((data_2d,np.array(row)))

    # print(data_2d)

f.close()

x = []
for i in range(0, 35):
    x.append(data_2d[i, 0])

# x = np.array([i for i in range(0, 35)])

active_cases = []
for i in range(0, 35):
    active_cases.append(data_2d[i, 1])

active_cases = np.array(active_cases, dtype=float)

recovered = []
for i in range(0, 35):
    recovered.append(data_2d[i, 2])

recovered = np.array(recovered, dtype=float)

death = []
for i in range(0, 35):
    death.append(data_2d[i, 3])

death = np.array(death, dtype=float)

total = []
for i in range(0, 35):
    sum = active_cases[i] + recovered[i] + death[i]
    total.append(sum)

total = np.array(total, dtype=float)


#plot 1: 

plt.subplot(2, 3, 1)

plt.pie(active_cases, labels = x)
plt.title('Active cases')
plt.legend(x, loc='upper right')

#plot 2:

plt.subplot(2, 3, 2)

plt.pie(recovered)
plt.title('Recovered cases')


#plot 3:

plt.subplot(2, 3, 3)

plt.pie(death)
plt.title('Death')

#plot 4

plt.subplot(2, 3, (4, 7))

for i in range(0, 35):
    recovered[i] = (recovered[i]/total[i])*100
    death[i] = (death[i]/total[i])*100
    active_cases[i] = (active_cases[i]/total[i])*100

plt.bar(x, recovered)
plt.bar(x, active_cases)
plt.bar(x, death)
plt.xlabel("State/UT")
plt.ylabel("% of cases")

plt.legend(["Recovered", "Active cases", "Deaths"])

plt.suptitle('COVID Dataset')
plt.show()