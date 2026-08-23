
f = open("file.txt")

# fileLine1 = f.readline()
# print(fileLine1, type(fileLine1))

# fileLine2 = f.readline()
# print(fileLine2, type(fileLine2))

# fileLine3 = f.readline()
# print(fileLine3, type(fileLine3))

# fileLine4 = f.readline()
# print(fileLine4, type(fileLine4))

# fileLine5 = f.readline()
# print(fileLine5, type(fileLine5))

# we can do this shit with loop as well


line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close() # this is compulsory, whenever you open a file, you've to close it.
