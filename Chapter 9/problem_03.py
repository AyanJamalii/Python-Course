# Repeat program 4 for a list of such words to be censored

words = ["Bad", "Ponka", "ganda", "pagal", "bad", "ponka", "Ganda", "Pagal"]

with open("file.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "*" * len(word))

with open("file.txt", "w") as f:
     f.write(content)
     print("File Updated.")