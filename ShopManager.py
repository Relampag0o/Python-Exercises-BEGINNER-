class EProduct():
    def __init__(self,name,prize,stock):
        self.name = name
        self.prize = prize
        self.stock = stock

    def showInfo(self):
        print(f"Product:  {self.name}   prize:  {self.prize}  stock:  {self.stock}")



class Shop():
    def __init__(self):
        self._products = []
        
    def addProduct(self,p):
        if not self._products.__contains__(p):
            self._products.append(p)
        else:
            print("The product is already contained.")

    def showProducts(self):
        for i, product in enumerate(self._products):
            print(f"Index: {i}  Product: {product.name} prize: {product.prize} stock: {product.stock} ")

    def sellProduct(self,productName,amount):
        for p in self._products:
             if p.name == productName:
                if (p.stock - amount >=0):
                    p.stock = p.stock - amount
                    print("The purchase was successfull.")
                else:
                    print("You cant sell the product because there arent enough units!")    
         


s = Shop()
s.addProduct(EProduct("phone",600,50))
s.addProduct(EProduct("mouse",50,100))
s.addProduct(EProduct("bottle",10,500))


choice = -1

def createProduct():
    print("Insert the name of the product: ")
    pName = input()
    print("Insert the prize of the product: ")
    pPrize = int(input())
    print("Insert the stock of the product: ")
    pStock = int(input())
    return EProduct(pName,pPrize,pStock)

def sellProduct(s):
    try:
        print("Insert the name of the product that you`d like to sell: ")
        pName = input()
        print("Insert the quantity of the product that you`d like to sell: ")
        quantity = int(input())
        s.sellProduct(pName,quantity)
    except:
        print("The name or either the quantity are wrong. Try again later.")
    

try:
    while(choice!=0):
        print("What would you like to do?")
        print("1. Add product")
        print("2. Show products")
        print("3. Sell product")
        print("0. Exit program.")
        choice = int(input())
        
        match choice:
            case 1:
                print("--- SELLING PRODUCT ---")
                s.addProduct(createProduct())
                
            case 2:
                print("Showing products..")
                s.showProducts()

            case 3:
                sellProduct(s)

            case _:
                print("Exiting program..")
except:
    print("There was an error with the option selected.")            
                

        



            
            
               
