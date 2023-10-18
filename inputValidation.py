

try:
    n = int(input("Insert an integer: "))
    print( f"{n} is an int!")
except ValueError:
    print("The input is not an int!")
