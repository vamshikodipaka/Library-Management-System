from LibraryMS.Books import book1
from LibraryMS.Member import Book
from LibraryMS.Person import Person

class Librarian(Person):
    library_collection = []

    def __init__(self, name, email, employee_id):
        self.name = name
        self.email = email
        self.employee_id = employee_id

    def add_book(self, book):
        self.library_collection.append(book)
        print(book.title + " is been added to lib_collection")

    def remove_book(self, book):

        if book in self.library_collection:
            self.library_collection.remove(book)
            print(book.title +" is been removed from the lib_collection")
        else:
            print(book.title + " not found in the lib_collection")

    def __str__(self):
        return self.name, self.employee_id

lib1 = Librarian("Shyam", "shyam@isr", "123678")

book2 = Book("robot5", "lino5", "xyz5", 5)
book3 = Book("robot6", "lino6", "xyz6", 4)

lib1.add_book(book1)
print(book1.title)

lib1.add_book(book2)
print(book2.title)

lib1.add_book(book3)
print(book3.title)

lib1.remove_book(book3)
print(book3.title)

lib1.remove_book(book3)
print(book3.title)