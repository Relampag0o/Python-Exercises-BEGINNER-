califications=[1,3,4,5,10,9]
print("Insert the index to check the calification contended: ")
index = int(input())

print("Insert the index to check the calification: ")

try:
    print(califications[index])
except IndexError:
    print("Error index out of bound. ")

