def myFun(*argv):
    for arg in argv:
        print(arg)

    print(argv[0])

myFun("ssl", "proj", "ecomm")

def myFun22(**kwargs):
    for thing in kwargs.items():
        print(thing[0]+" "+thing[1])

myFun22(first='Geeks', mid='for', last='Geeks')