import enchant
d = enchant.Dict("en_US")
file = open("/Users/swethaa/Desktop/Home/hey.txt", "r")
splitfile = file.read()
convertlist = splitfile.split()

misspelled = []
for eachword in convertlist:
    if d.check(eachword):
        None
    else:
        misspelled.append(eachword)
print("The misspelled words are: ")
print(misspelled)
