# import SSLmodule as fx
import math
from SSLmodule import SSLadd

# print(SSLadd(5, 7))

# for x in range(0.006, 0.09, 0.005):
#     print(x)
# the above code gives error

xs = [x * 0.005 for x in range(2, 19)]

# for i in xs:
#     print(((math.e**i) - 1)/i)

for i in range(99999, 999, -10000):
    print((1 + 1/i)**i)