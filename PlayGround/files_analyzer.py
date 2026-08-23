import os

file_path = input("Enter text File Path: ")

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        lines = content.splitlines()
        print(f"total lines : {len(lines)}")

        words = content.split()
        print(f"Total words in the file are: {len(words)}")

        char = len(content)
        print(f"Total Characters in the file are: {char}")
        
else: 
    print("File not Found.")


    