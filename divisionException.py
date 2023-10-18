

print("Insert the first number: ")
n = int(input())
print("Insert the second number: ")
n2 = int(input())

try:
    print(n/n2)
except ZeroDivisionError:
    print("You cant / between 0")    

