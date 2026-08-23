f = open("file.txt")
print(f.read())
f.close()

# Same thing can be written as with statement, so we dont have to write close() .

with open("file.txt") as f:
    print(f.read())

