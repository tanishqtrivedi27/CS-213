class Student:

    def __init__(self, name, rollno, cpi):
        self.name = name
        self.rollNo = rollno
        self.CPI = cpi

    def __str__(self):
        str = "Roll number {} has CPI {} and name {}"
        return str.format(self.rollNo, self.CPI, self.name)

student_list = []

f = open(r"C:\Users\Tanishq\Semester 3\CS213-SSL-Assignments\python\210010056-old\data.txt", "r")

# reading the data from data.txt
for i in range(70):
    f_c = f.readline()
    f_c = f_c.split(",")
    student_list.append(Student(f_c[1], f_c[0], float(f_c[2][0:3]))) #appending student list

f.close()

for i in student_list:
    print(i)

#list comprehension
f = open(r"C:\Users\Tanishq\Semester 3\CS213-SSL-Assignments\python\210010056-old\data.txt", "a")

def max(lis):
    maxt = lis[0]
    for i in range(70):
        if (lis[i] > maxt):
            maxt = lis[i]

    return maxt

y = [i.CPI for i in student_list]
z = [i.name for i in student_list if i.CPI == max(y)]

f.write("\n")
f.write(z[0])



# average cpi
x = [i.CPI for i in student_list]
sum = 0
for i in x:
    sum = sum + i

cpi_avg = str(sum/len(x))
f.write("\n")
f.write(cpi_avg)

f.close()