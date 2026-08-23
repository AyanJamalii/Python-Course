try:
    a = int(input("hey, Enter any Number: "))
    print(a)

except ValueError as v:
    print(v)


except Exception as e:
    print("Bhai number bola hai dalne ko.")
    print(e)

    # Alag alag specific types k bh error hote hain, mention in handbook.

