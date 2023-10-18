class Book:
    def __init__(self,name,author):
      self._name = name
      self._author = author
      self._status = True

    def borrow(self):
        status = False

    def returnBook(self):
        self.status = True

    def __str__(self):
        return f"Book name:  {self._name}  Author:  {self._author}   status:   {self._status}"
       
class Library:
    def __init__(self):
        self._books=[]

    def addBook(self,book): 
        self._books.append(book)

    def deleteBook(self,book):
        if (self._books.__contains__(book)):
              self._books.remove(book)
        else:
            print("The book is not contained in the library. Try again!")        

    def showBooks(self):
        
        if (len(self._books)>0):
            for book in self._books:
                print(book)

library1 = Library()

book1 = Book("El Gran Gatsby", "F. Scott Fitzgerald")
book2 = Book("Cien años de soledad", "Gabriel García Márquez")
book3 = Book("Matar un ruiseñor", "Harper Lee")


library1.addBook(book1)
library1.addBook(book2)
library1.addBook(book3)
library1.showBooks()

