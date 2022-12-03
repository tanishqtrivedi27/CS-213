import numpy as np

arr = np.random.randint(0, 10, (2, 3, 4))
print(arr)

# 1.a 
sum = 0
for i in np.nditer(arr):
    sum = sum + i

print("Answer to question 1 A")
print(sum)

# 1.b 

mei = np.mean(arr, dtype='int')
print("Answer to question 1 B")
#mean * number of elements
print(mei*24)

#2 
arr2 =arr.reshape(-1)
me = np.mean(arr,dtype='int')
print("Answer to question 2")
print(np.searchsorted(arr2, me))

#3
arr3 = np.vstack((arr[0, 1, 2:], arr[0, 2, 2:]))

arr4 = np.vstack((arr[1, 1, 0:2], arr[1, 2, 0:2]))
print("Answer to question 3")
arr5 = np.concatenate((arr3, arr4), axis=1)
print(arr5)

#4
arr3 = np.stack((arr[0, 1, 2:], arr[0, 2, 2:]), axis=1)

arr4 = np.stack((arr[1, 1, 0:2], arr[1, 2, 0:2]), axis=1)
print("Answer to question 4")
arr5 = np.concatenate((arr3, arr4), axis=1)
print(arr5)