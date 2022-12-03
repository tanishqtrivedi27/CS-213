import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos


def fib(x):
    if (x == 0 or x == 1):
        return x
    
    return fib(x-1) + fib(x-2)

#plot 1:

lis33 = []
for i in range(0,14):
    lis33.append(i)

x = np.array(lis33)

lis97 = [fib(i) for i in lis33]
y = np.array(lis97)

plt.subplot(2, 1, 1)
plt.grid(color='y', ls='dashed')
plt.ylabel('Fibonacci number', color='g')
plt.plot(x,y, marker = 'o', mec='#000000', mfc = 'r', ls = 'dotted', c='#000000')

#plot 2:
lis0 = []
for i in range(0,101,1):
    lis0.append(i)

x = np.array(lis0)
lis = [cos(i) for i in lis0]
lis2 = [sin(i) for i in lis0]
y = np.array(lis)
z = np.array(lis2)


plt.subplot(2, 1, 2)
plt.grid(color='y', ls='dashed')
plt.xlabel('x ', color='g')

plt.plot(x,y, c='#000000', label='cos') # cos
plt.plot(x,z,  ls='dotted',c='#000000', label='sin') #sin
plt.legend(loc='lower left')


plt.suptitle('Functions', color='b')

plt.show()

# plt.title("XY- plotting")
# plt.xlabel("X coordinate")
# plt.ylabel("Y coordinate")
# plt.plot(x, y, marker = 'o', ms=10, mec='r', mfc = 'b', ls = 'dotted', c='y', lw=5)
# #marker type , marker size, marker edge color, marker face color(inside), linestyle, linecolor, linewidth

# plt.show()

# marker|line|color
# plt.plot(x, y, '*--r')

