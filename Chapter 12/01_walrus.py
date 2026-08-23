# using Walrus operator. ":"

if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"The list to long, [{n} elements, Expected => 3 ]")
