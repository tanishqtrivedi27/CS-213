def f13_ana(str1, str2):
    thisdict = {}
    thisdict2 = {}
    
    for i in str1:
        if(thisdict.get(i) == None):
            thisdict[i] = 1
        else:
            thisdict[i] += 1

    for i in str2:
        if(thisdict2.get(i) == None):
            thisdict2[i] = 1
        else:
            thisdict2[i] += 1


    for i in thisdict:
        if(thisdict[i] == thisdict2[i]):
            continue
        else:
            return False

print(f13_ana("binary", "brainy"))