import os
import random

print("Insert the path of your file: ")
path = input()
if (os.path.isfile(path)):
    f = open(path,"w")
else:
    f = open(path,"x")    
print("Insert the amount of numbers: ")
amount = int(input())
for i in range (1,amount):
    f.write(str(random.randint(0,200))+ '\n')

print("The process is done!")
    