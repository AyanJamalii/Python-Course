expenses = []

while(True):
    print(f"\n1. Add Expense")
    print(f"2. View all Expenses")
    print(f"3. Exit")

    choice = int(input("Enter what you want to do (1-3): "))

    if(choice == 1):
        item = input("Enter the Item's Name: ") 
        amount = int(input("Enter Item's Price: "))
        expenses.append({"Item" : item, "Price": amount })
        print(f"{item} Added to Expenses.")

    elif(choice == 2):
        if not expenses:
            print("No Expenses Added Yet.")
        else:
            print(f"\n ---- YOUR EXPENSE LIST ----")
            for i in expenses:
                print(f"Item: {i['Item']} | Price: {i['Price']} Rs.")
    elif(choice == 3):
        print("Expense Tracker Closed.")
        break
    else:
        print("Invalid Choice, Please choose between (1-3): ")

    

