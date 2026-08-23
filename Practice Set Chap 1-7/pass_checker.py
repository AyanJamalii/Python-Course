while True: 
    password = input("Enter a password: ")
    if len(password) >= 8 and any(c.isdigit() for c in password):
        print("Password set Successfully! ")
        break
    else:
        print("Passoword didn't meet the Requirements.")

