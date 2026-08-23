# . Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
    "gaane" : "Song",
    "bhago" : "Run",
    "sojao" : "Sleep",
    "uthjao" : "Wake up"
}

word = input("Enter the word you want the meeaning of: ")
print(words[word])
