from functools import reduce 

l = [1, 2, 3, 4, 5]

squares = lambda x: x*x

sqList = map(squares, l)
print(list(sqList))


# FILTER EXAMPLE 

def even(n):
    if (n%2 == 0):
        return True
    return False

evenNums = filter(even, l)
print(list(evenNums))

# REDUCE EXAMPLE

def sum(a, b):
    return a + b

print(reduce(sum, l))