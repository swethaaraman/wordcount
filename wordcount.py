file = open("/Users/swethaa/Desktop/Home/untitled.txt", "r")
splitfile = file.read()
splitfile = splitfile.lower()
convertlist = splitfile.split()
di = {}
for eachWord in convertlist:
    di[eachWord] = di.get(eachWord, 0) + 1
converttolist = []
for key, values in di.items():
    converttolist.append((values, key))
converttolist.sort()
print(converttolist)
