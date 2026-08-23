while True:
    
    try:
        num_1 = int(input("Enter Any Number: "))
        num_2 = int(input("Enter Second Number: "))

        operations = int(input("Press 1 for '+', 2 for '-', 3 for '*', 4 for '/': "))


        if operations == 1:
            output = num_1 + num_2
            print(f"The Sum of the number {num_1} & {num_2} is {output}")
        elif operations == 2:
            output = num_1 - num_2
            print(f"The Minus of the number {num_1} & {num_2} is {output}")
        elif operations == 3:
            output = num_1 * num_2
            print(f"The Product of the number {num_1} & {num_2} is {output}")
        elif operations == 4:
            if num_2 == 0:
                print("You cant divide anything with Zero (0).")
            else:
                output = num_1 / num_2
                print(f"The Division of the number {num_1} & {num_2} is {output}")
        else:
            print("Invalid operation choice!")

    except ValueError:
        print("Please enter only Numbers.")

    choice = input("Do you want to calculate again? (y/n): ")
    if choice.lower() == "n":
        break