class books:

    def __init__(self, name, author, publisher):
        self.name = name
        self.author = author
        self.publisher = publisher

    def __str__(self):
        # return f"Book name: ({self.name}). Author: ({self.author}). PUblisher: ({self.publisher})"
        return "Book name: ({}). Author: ({}). PUblisher: ({})".format(self.name, self.author, self.publisher)


mylist = []
book1 = books('TAOCP', 'D. Knuth', 'Addison-Wesely')
book2 = books('Introduction to Algorithms', 'Cormen', 'MIT Press')
book3 = books('Probablity Introduction', 'Gaze Schay', 'Addison-Wesely')
book4 = books('Discrete Math', 'Rosen', 'McGraw Hill')
book5 = books('Operating System', 'W stallings', 'Pearson')
book6 = books('Networking', 'Foruzen', 'Pearson')

mylist.append(book1)
mylist.append(book2) 
mylist.append(book3)
mylist.append(book4)
mylist.append(book5)
mylist.append(book6)

for i in mylist:
    # print(i)
    pass

class Student:
    studentName = ""
    studentIdNumber = 0

    def __init__(self, param1, param2):
        self.studentIdNumber = param2
        self.studentName = param1

    def display(self):
        print(f"Name - {self.studentName}. ID - {self.studentIdNumber}")


class BTech(Student):
    def __init__(self, p1, p2, p3, p4):
        self.yearOfAdmission = p1
        self.department = p2
        Student.__init__(self, p3, p4)