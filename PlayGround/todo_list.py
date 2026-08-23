import os

while True:
    print("\nToDo List")
    print("1. View Task")
    print("2. Add New Task")
    print("3. Clear All Tasks")
    print("4. Exit")
    choice = input("\nChoose an option (1-4): ").strip()

    if choice == "1":
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r")as r:
                tasks = r.read()
                if tasks.strip():
                    print(f"These are your tasks: {tasks}\n")
                else:
                    print("Your ToDo list is Empty.")
        else:
            print("File Didn't Exist.")
    elif choice == "2":
        user_task = input("Enter Your task you want to add: ")
        with open("tasks.txt", "a") as t:
            t.write(user_task + "\n")
        print("Task Added Sucessfully.")
    elif choice == "3":
        with open("tasks.txt", "w") as w:    
            w.write(" ")
        print("All Tasks Cleared.")
    elif choice == "4":
        print("GoodBye!")
        break
    else:
        print("Invalid Choice please choose between (1-4)")
        