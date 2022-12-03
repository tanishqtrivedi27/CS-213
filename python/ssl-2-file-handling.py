theLines = ["This is IIT-DH \n", "This is CSE \n", "This is 2022 \n", "This isSP16 \n"]

with open(r"210010056-SSL-2022OCT02.txt", "w")as f:
    f.write("Hello SSL\n")
    f.writelines(theLines)

f = open("210010056-SSL-2022OCT02.txt", "r")
print(f.readline())
print(f.read(15))
f.close()
# You can return one line by using the readline() method: