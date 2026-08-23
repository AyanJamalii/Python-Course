# Create a class “Programmer” for storing information of few programmers working at Antropic.

class Programmer:
    company = "Antropic"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a = Programmer("MAJ", 2200000, 222222) # Salary ko idhr pass nh kia q k woh tu sare employee ki same hogi na isi liye, but har employee ka name and salary wagera diff hoga tu   isi liye usko alag se pass kia as an instance.
print(a.company, a.name, a.salary, a.pin)