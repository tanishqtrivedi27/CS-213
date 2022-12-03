import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr1[0,0] , arr1[0,1] = arr1[0,1] , arr1[0,0]
arr1[1,0] , arr1[1,1] = arr1[1,1] , arr1[1,0]
print(arr1)


print(np.random.random(size = (5, 3)))

# random.randint(low, high=None, size=None, dtype=int)
print(np.random.uniform(5, 10, size=(5, 3)))