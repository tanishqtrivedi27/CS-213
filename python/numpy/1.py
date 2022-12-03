import numpy as np
arr = np.full((3, 3), True)
print(arr)

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

for i in np.nditer(arr2):
    if (i%2!=0):
        print(i)

# sum = 1
# for i in arr2.shape:
#     sum = sum*i


# for i in range(0, sum):
#     if (arr2.reshape(-1)[i]%2!=0):
#         arr2.reshape(-1)[i] = -1


x = np.where(arr2 %2 != 0)

np.put(arr2, x, -1)
print(arr2)
print(arr2.reshape(2, 4))



# nditer
# ndim
# shape
# reshape
