import numpy as np 
arr = np.array([1,2,3])
arr2 = np.dstack((arr, arr, arr))

print(arr2.reshape(-1))

arr3 = np.concatenate((arr2.reshape(-1), arr, arr, arr))
print(arr3)