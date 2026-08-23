def plus(a, b):
    return a + b

def mius(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): 
    if b == 0:
        return "ERROR: Can't Divide by Zero (0)"
    return a / b

operations = {
    "+": plus,
    "-": mius,
    "*": multiply,
    "/": divide
}

def calculator():
    while True:
        try:
            num_1 = float(input("Enter first Number: "))
            op = input("Select any operation +, -, *, / : ")
            if op not in operations:
                print("Select any 1 from these +, -, *, / : ")
                continue

            num_2 = float(input("Enter second number: "))

            result = operations[op](num_1, num_2)
            print(f"{num_1} {op} {num_2} = {result}")

        except ValueError:
            print("Enter a valid NUMBER.")

        if input("\nCalulate again (y/n): ").lower() == "n":
            print("GoodBye!")
            break

calculator()