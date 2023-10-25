import random
import numpy as np

# filling the array with random numbers using numpy (had to install the package somehow)
swaps = np.full(256,-1)


def shuffle():
    random.seed(5)
    for i in range(len(swaps)):  
        rand = random.randint(0, 255) 
        while find(rand):
            rand = random.randint(0, 255)  
        swaps[i] = rand 


def find(value):
    for i in swaps:
        if (i==value):
            return True
    return False 


def showSwaps():
    for i in swaps:
        print(i)




shuffle()
showSwaps()


