class Employee:
    name = "Ayan"
    language = "Python" # This is the class attribute.
    salary = 2200000

# YE "__ (underscore)" wale methods ko dunder methods kaha jata hai, Inko neeche end me call krne ki zarort nh ha just like other functions, ye khud hi automatically run hojate hai. Sare automatically run nh hote sirf __init__ run hota hai.

    def __init__(self, name, salary, language):         
        self.name = name
        self.salary = salary
        self.language = language
      # idhr me ne neeche employee me instance attr k through new values di hai jinko me init function me argument k through run kar wa raha ho, so ab ye print hoga porana wala nhi.


    def getInfo(self): # idhr hum self ko pass kr rhe hai or neeche ussi ko use.
        print(f"My name is {self.name}. My Language is {self.language} and My Salary is {self.salary}.")
    

    @staticmethod
    def greet():
        print("GOOOD MORNING..... <3")

ayan = Employee("MAJ", 1800000, "Pythonnnn") # idhr me direct instance attr de rha ho tu ab direct ye print honge from __init__ function. 
# ayan.name = "Ayan the OG." # this is the instance attribute.
print(ayan.language, ayan.salary, ayan.name)    