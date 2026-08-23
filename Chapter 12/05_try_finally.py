def func():
    # Finally jab use karte hai jab hum function me hon.    

    try:
        a = int(input("hey, Enter any Number: "))
        print(a)
        return

    except Exception as e:
        print("Bhai number bola hai dalne ko.")

    finally: 
        print("we're inside the fianlly.") # ye chalega hi chalege bhale try wala block sucessfully run ho ya na ho, ya retrun hu q na kardo ye run hoga.

func()