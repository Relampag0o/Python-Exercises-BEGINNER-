class customDivisionException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

try:
    print("Insert the first number: ")
    n = int(input())
    print("Insert the second number: ")
    n2 = int(input())
    if (n2<=0):
        raise customDivisionException("You cant divide between 0..!")
    else:
        print(n/n2)   
except customDivisionException as c:
    print(c)





