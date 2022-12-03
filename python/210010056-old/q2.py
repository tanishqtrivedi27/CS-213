thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "idk": "rtx"
}

x = list(thisdict.keys())
# sorted by keys
x.sort()
for i in x:
    print(i, thisdict[i])


# sorted by values
x = list(thisdict.items())

