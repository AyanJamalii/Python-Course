# 1. Write a program to print multiplication table of a given number using for loop.

tables_input = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{tables_input} X {i} = {tables_input * i}")
    