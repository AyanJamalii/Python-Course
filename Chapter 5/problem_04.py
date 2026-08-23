# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {} # khali dictionary banae.

name = input("Enter your name: ") # user se input me naam lega.
lang = input(f"hey {name}, Enter your Favourite programming Language: " ) # favourite lang lega
d.update({name: lang}) # idhr Update method ki madad se usse dictionary me add krde ga. 

name = input("Entey your name: ")
lang = input(f"Hey {name}, Enter your favourite programing language: ")
d.update({name : lang})

name = input("Entey your name: ")
lang = input(f"Hey {name}, Enter your favourite programing language: ")
d.update({name : lang})

name = input("Entey your name: ")
lang = input(f"Hey {name}, Enter your favourite programing language: ")
d.update({name : lang})

name = input("Entey your name: ")
lang = input(f"Hey {name}, Enter your favourite programing language: ")
d.update({name : lang})

print(d)