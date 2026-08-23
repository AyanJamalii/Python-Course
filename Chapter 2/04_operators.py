"""
Following are the common operators in Python.

1. Arithmatic Operators: + , - , * , / , etc. ----> koi bh arimatic calculation k liye use hote hai.

2. Assingments Operator: = , += , -= , etc ---> Kisi bh variable ko kuch bh assign karne k liye use kia jata hai, like A = 18. A ko 18 value assign kr di gayi hai. 

3. Comparison Operators: ==, >, >=, <, != etc ----> Ye 2 variables k beech me comparison krne k liye use hote hai

4. Logical Operators: and, or, not. -----> neeche example hai.
"""

# Arithmatic Operator: 

a = 18
b = 22

c = a - b
print(c) 

# Assignment Operators:

a = 18 - 18 # a ko jo value di gayi ha usme se minus krdo agli value, here it is 18 - 18 so the result will be 0. 
print(a)

b = 22

b += 18 # idhr hum b ki jo orginal value hmne uper wali line me di ha usko aik new value assign krwa rahe hai, so the orginal value is 22 and usme 18 plus kar wa rahe hai so the ans will 40. and idhr hum kuch bh use kr sakte hain not only +, we can use - , * , /  etc.

print(b)

# Comparison Operators: they just answer in boolens in a form of TRUE & FALSE.

d = 2>2
e = 2<2
f = 2!=2
j = 2>=2
h = 2==2

print(d)
print(e)
print(f)
print(j)
print(h)

# Logical Operators: 
# Truth Table

# Truth Table of 'or'
x = True or False
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth Table of 'and'
y = True or False
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

# there is not operator as well but its not like 'and & or', it just works on single boolean.
print(not(True)) # abh ans false ayega.
print(not(False)) # abh ans True ayega.