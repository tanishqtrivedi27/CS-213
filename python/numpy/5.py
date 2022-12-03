import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(np.intersect1d(a, b))


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

print(np.setdiff1d(a, b))


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])


print(np.where(np.equal(a, b)))

a = np.array([2, 6, 1, 9, 10, 3, 27])
a = np.delete(a, np.where(a>10))
print(a[np.where(a>5)])