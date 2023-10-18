
try:
    print("Insert a number:")
    # insert a float to make the exception pop up 
    n = int(input())
except ValueError:
    print("The conversion is not valid for this number.")