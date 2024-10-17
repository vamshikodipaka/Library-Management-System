from LibraryMS.Person import Person
from LibraryMS.Books import Book


class Member(Person):
    borrowed_books = []

    def __init__(self, name, email, member_id):
        self.name = name
        self.email = email
        self.member_id = member_id

    def borrow_book(self, book):
        if book.copies_available > 0:
            book.copies_available -= 1
            self.borrowed_books.append(book)
            return True
        else:
            print(book.title + " is not currently available")
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.copies_available += 1
            self.borrowed_books.remove(book)
            return True
        else:
            print(book.title + " is not been borrowed")
            return False

    def __str__(self):
        borrowed_books = ", ".join(book.title for book in self.borrowed_books)
        return self.name, self.member_id, borrowed_books


member1 = Member("Ram", "ram@isr", 12345)
book2 = Book("robot2", "lino2", "xyz2", 5)
book3 = Book("robot3", "lino3", "xyz3", 4)

if member1.borrow_book(book2):
    print(book2.title + " book is been borrowed")
if member1.borrow_book(book3):
    print(book3.title + " book is been borrowed")
if member1.return_book(book3):
    print(book3.title + " book is been returned")

print(member1.__str__())
member1.__str__()