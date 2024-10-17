# Library-Management-System

## Task: Library Management System

## Scenario:
You are tasked with designing a simple Library Management System using Object-Oriented Programming (OOP) principles. The system should be able to manage books, members, and staff in a library. The goal is to test your understanding of key OOP concepts like classes, objects, inheritance, polymorphism, abstraction, and encapsulation. You are required to model the system based on the following specifications.

## Requirements:
### Book Class:

### Attributes: title, author, isbn, copies_available
### Methods:
__init__: Initializes a new book object with its title, author, ISBN, and available copies.
borrow_book(): Reduces the number of available copies by 1 if the book is available.
return_book(): Increases the number of available copies by 1 when a book is returned.
__str__: Returns a string representation of the book (e.g., title and author).
Person Class (Base Class):

### Attributes: name, email
### Methods:
__init__: Initializes a person with a name and email.
__str__: Provides a string representation of the person.
Member Class (Inherits from Person):

### Attributes: name, email, member_id, borrowed_books (a list to store books borrowed by the member)
### Methods:
__init__: Initializes a member with a name, email, and member ID. Initializes borrowed_books as an empty list.
borrow_book(book): Allows the member to borrow a book, ensuring that the book is available (using Book class method). Adds the book to the member’s borrowed_books list.
return_book(book): Allows the member to return a book, removing it from the borrowed_books list.
__str__: Overrides Person's __str__ to also display the member's ID and list of borrowed books.
Librarian Class (Inherits from Person):

### Attributes: name, email, employee_id
### Methods:
__init__: Initializes a librarian with a name, email, and employee ID.
add_book(book): Adds a new book to the library's collection.
remove_book(book): Removes a book from the library's collection if it exists.
__str__: Overrides Person's __str__ to also display the employee ID.
Library Class (Abstraction and Encapsulation):

### Attributes: books, members, librarians
### Methods:
__init__: Initializes the library with an empty list of books, members, and librarians.
add_member(member): Adds a new member to the library.
add_librarian(librarian): Adds a new librarian to the library.
search_book_by_title(title): Returns a book object if the title matches one in the collection, or returns a message indicating the book is not available.
search_book_by_author(author): Returns a list of books by a given author, or a message indicating no books by that author are found.
display_all_books(): Displays all books currently in the library.
## Example Interactions:
A librarian adds books to the library.
A member searches for a book and borrows it.
If a book is unavailable, the system should notify the member that it is not available.
The member returns the book, and the book’s availability is updated.
The librarian can remove books from the system.
Additional Concepts to Implement:
### Polymorphism: Ensure that both the Member and Librarian classes provide customized implementations of the __str__ method to showcase polymorphism.
### Encapsulation: Keep attributes like copies_available, borrowed_books, etc., private and provide getter and setter methods if needed.
### Abstraction: The Library class abstracts away the complex operations of managing members, books, and staff, only exposing necessary methods to interact with the system.

## Task Goals:
### Classes and Objects: Demonstrate how to create and use classes and objects.
### Inheritance: Show inheritance between Person, Member, and Librarian classes.
### Polymorphism: Demonstrate how methods can be overridden in subclasses and used in a polymorphic way.
### Encapsulation: Properly encapsulate data and expose it via methods.
### Abstraction: Use the Library class to hide complex functionality and expose simple methods.

## Bonus (Optional):
Add functionality for tracking due dates for borrowed books and issuing reminders for overdue books.
Introduce fines for late returns and track member payment history.
Evaluation Criteria:
Correct implementation of OOP concepts.
Clear and well-documented code.
Proper handling of edge cases (e.g., borrowing books when none are available).
Thoughtful design and use of class relationships.
