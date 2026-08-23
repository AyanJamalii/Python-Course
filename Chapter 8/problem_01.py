# Write a python program using function to convert Celsius to Fahrenheit.

def f_to_c(f):
    return 5*(f-32)/9  # 5*(f-32)/9 ---> Formula to convert farenheit into celsius, f stands for the number you want to convert.


f = int(input("Enter the Temperature in F: "))
c = f_to_c(f)

print(f"{f}°F into Celcius is {round(c, 2)}°C.")