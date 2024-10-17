from LibraryMS.Books import Book, book1
from LibraryMS.Member import Member, book3, member1
from LibraryMS.Librarian import lib1

class Library:
    books = []
    members = []
    librarians = []

    def __init__(self, books, members, librarians):
        self.books = books
        self.members = members
        self.librarians = librarians

    def add_member(self, member):
        self.members.append(member)

    def add_librarian(self, librarian):
        self.librarians.append(librarian)

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def search_book_by_author(self, author):
        return (book for book in self.books
                if book.author.lower() == author.lower())

    def display_all_books(self):
        if not self.books:
            print("No books available in the library")
        else:
            print("Library Books:")
            for book in self.books:
                print(book.title + " written by " + book.author)

lib= Library([book1,book3], [member1], [lib1])

x= lib.search_book_by_title("robot3")
print(x)

y=lib.search_book_by_author("lino")
for book in y:
    print(book.title)

lib.display_all_books()