try:
    print("Insert the name of your file to read it: ")
    f = open(input(),"r")
    print(f.read())
except FileNotFoundError:
    print("Sorry, the file is not valid. Try again later.")    
