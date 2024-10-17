
class Book:
    def __init__(self, title, author, isbn, copies_available):
        self.title =  title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available

    def borrow_book(self, available=None):
        if available:
            self.copies_available -= 1
        return self.copies_available

    def return_book(self, returned=None):
        if returned:
            self.copies_available += 1
        return self.copies_available

    def __str__(self):
        return (self.title + " by " +  self.author)


book1 = Book("robot","lino", "xyz1", 10)
bookX = book1.borrow_book(available=True)
print(bookX)
bookX = book1.return_book(returned=True)
print(bookX)
print(book1.title)
print(book1.__str__())
