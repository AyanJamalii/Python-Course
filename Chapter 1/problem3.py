import os

#specify the Directory you want to list. 
directory_path = '..//Chapter 1'

# it will list all the directories in the specific path
contents = os.listdir(directory_path)

# Printing the contents in the directory.
print(contents)
