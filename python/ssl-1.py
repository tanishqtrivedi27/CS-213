import math

def f01_IED(num):
    mylist = []
    while(num):
        mylist.append(num%10)
        num = int(num/10)

    mylist = [(x+1)%10 for x in mylist]
    num=0
    for i in range(0, len(mylist)):
        num = num+(mylist[i]*(10**i))

    return num


def f02_LPD(num):
    mylist = []
    for i in range(num-1, 0, -1):
        if (num % i ==0):
            mylist.append(i)

    print(mylist)

str = "abcdefghijklmnopqrstuvwxyz"
def f03_BPIS(str, num):
    for i in range(0, len(str)):
        if ((i+1) % num == 0):
            print(str[i])
        else:
            print(str[i], end="")

def f04_genFunc(i):
    if (i == 0):
        return -2

    return (3*(f04_genFunc(i-1)**2) + 2*f04_genFunc(i-1) + 7)%10

y = lambda x : f04_genFunc(x)**2

# for i in range(0, 7):
#     print(y(i))

# print(math.factorial(100))

# By default Python‘s print() function ends with a newline.
#  A programmer with C/C++ background may wonder how to 
# print without a newline. Python’s print() function 
# comes with a parameter called ‘end‘. 
# By default, the value of this parameter is ‘\n’, i.e. the new line character. 

f03_BPIS(str, 4)

lis = []