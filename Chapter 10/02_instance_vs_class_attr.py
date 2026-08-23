class Employee:
    name = "Ayan"
    language = "py" # This is the class attribute.
    salary = 2200000

ayan = Employee()
ayan.name = "Ayan the OG." # this is the instance attribute.
print(ayan.language, ayan.salary, ayan.name)

# Here mene name ko 2 dafa define kia ha, 1st as an class attr and 2nd as an instance atter, now the 2nd one will print, cuz the instance attributes take preference over class attributes. 
