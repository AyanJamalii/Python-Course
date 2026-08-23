# IF ELSE ELIF LADDER.

a = int(input("Enter your age: "))

if(a>=18):
    print("You're 18")
elif(a<0):
    print(f"You're {a}! Konsi duniya se aye ho?")
elif(a==0):
    print(f"{0} isn't a valid age.")
else:
    print("Sorry! You're below 18.")
