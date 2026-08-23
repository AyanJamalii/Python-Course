st = "No, Ayan is a good boy."

file = open("myFile.txt", "w")  # kisi or file ka naam deta tu us name ki file create ho jati.

file.write(st)

file.close() # this is compulsory, whenever you open a file, you've to close it.