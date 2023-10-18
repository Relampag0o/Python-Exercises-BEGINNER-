import os

def createFile():
    print("Insert the file name: ")
    filename = input()

    if os.path.isfile(filename):
        return open(filename, "a") 
    
    else:
        return open(filename, "x")
   




def addTask(f):
    print("Insert your task: ") 
    f.write(input())
    print("The task has been added successfully!")
    f.close()
    
 
choice = 1

f = createFile()

while (choice!=0):
    print("What would you like to do?: ")
    print("1. Add task")
    print("2. List tasks")
    print("0. EXIT ")
    choice = int(input())

    match choice:
        case 0:
            print("Exiting program.. ")
        case 1:
            addTask(f)
        case 2:
            with open(f.name, "r") as file:
                content = file.read()
                print("Tasks:")
                print(content)

        case _:
            print("Unvalid command.. ")

