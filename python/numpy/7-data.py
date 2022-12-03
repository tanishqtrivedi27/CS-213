import csv
import numpy as np

f = open(r'C:\Users\Tanishq\Semester 3\CS213-SSL-Assignments\python\numpy\iris.data', 'r')

data2d = np.array([[]])
# with f:
#     # reader = csv.DictReader(f)
#     reader = csv.reader(f)
#     n1 = np.array(next(reader)[0:4] , dtype='f')
#     n2 = np.array(next(reader)[0:4] , dtype='f')
#     data_2d = np.vstack((n1, n2))
#     for row in reader:
#         data_2d = np.vstack((data_2d,np.array(row[0:4], dtype='f')))

#     print(data_2d)
    

with f:
    # reader = csv.DictReader(f)
    reader = csv.reader(f)
    n1 = np.array(next(reader))
    n2 = np.array(next(reader))
    data_2d = np.vstack((n1, n2))
    for row in reader:
        data_2d = np.vstack((data_2d,np.array(row)))

    print(data_2d)

f.close()