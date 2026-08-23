# class Employee:
#     name = "Ayan"
#     language = "py" # This is the class attribute.
#     salary = 2200000

#     def getInfo():
#         print(f"My name is {name}. My Language is {language} and My Salary is {salary}.")

# ayan = Employee()
# ayan.name = "Ayan the OG." # this is the instance attribute.
# print(ayan.language, ayan.salary, ayan.name)
# ayan.getInfo()

# Here ab agr me ye code Run kar rha hon tu mere pas ERROR arha hai k, "TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given" matlab ha k getinfo function me aik argument pass ho rha ha but use nh horha, ab woh hame nazar nh arha but while running it is running as "Employee.getInfo(ayan)" ayan pass ho rha jabhi error arha hai...

# Isi liye hum "self" ka use krte hai. new code:

class Employee:
    name = "Ayan"
    language = "Python" # This is the class attribute.
    salary = 2200000

    def getInfo(self): # idhr hum self ko pass kr rhe hai or neeche ussi ko use.
        print(f"My name is {self.name}. My Language is {self.language} and My Salary is {self.salary}.")
    
    # def greet(self): # Idhr "self" dena zarori ha bhale use karo ya nhi karo. otherwise error ayega.
    #     print("Goood Morningg.....")

    # agr Hame pora ka pora argument pass nh karna bcz woh use nh horha tu pass karna fazool but error ki wajah se krna parta hai, tu hum usko AS an "STATIC METHOD" mark kr dein ge, usse code ko pta chal jaye ga k isme kuch use nh horha hai.

    @staticmethod
    def greet():
        print("GOOOD MORNING..... <3")

ayan = Employee()
ayan.name = "Ayan the OG." # this is the instance attribute.
# print(ayan.language, ayan.salary, ayan.name)
ayan.getInfo() # ab run karoga tu ans proper aye ga.
ayan.greet
 
