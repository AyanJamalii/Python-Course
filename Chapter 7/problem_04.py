# 4. Write a program to find whether a given number is prime or not. ( prime num mtlb not divided by itself or 1)

n = int(input("Enter any number to check: "))

for i in range(2, n):
    if (n%2) == 0:
        print(f"{n} is not a prime number.")
        break
    else: 
        print(f"{n} number is prime")
        break
