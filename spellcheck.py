import enchant
import sys
d = enchant.Dict("en_US")
with open(sys.argv[1], 'r') as file:
    splitfile = file.read()
convertlist = splitfile.split()

errors = []
for eachword in convertlist:
    if d.check(eachword):
        None
    else:
        errors.append(eachword)
for eachmisspelledword in errors:
    suggestion = d.suggest(eachmisspelledword)
    print (eachmisspelledword, suggestion)
