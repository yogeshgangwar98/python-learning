
class Book:
    def __init__(self,title,author,price):
        self.title  = title
        self.author = author
        self.price  = price
    
    def display(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return "Book added successfully"
    
    def remove_book(self, title):
        if not self.books:
            return "Library is empty. No book found."
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"{title} removed successfully"
        return f"Book Not found with title: {title}"
    
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return f"Book Found:\n{book.display()}"
        return f"Book Not found with title: {title}"
    
    def display_books(self):
        for book in self.books:
            print(book.display())

    def most_expensive_book(self):

        if not self.books:
            return "No books available"

        expensive_book = max(
            self.books,
            key=lambda book: book.price
        )

        return expensive_book
library = Library()
 # Add books
library.add_book(Book("Python Basics", "Eric Matthes", 499))
library.add_book(Book("Clean Code", "Robert C. Martin", 799))
library.add_book(Book("FastAPI Mastery", "Bill Lubanovic", 649))
# Display all
library.display_books()
# Search
print(library.search_book("Clean Code"))
print(library.search_book("Django Unleashed"))  # not found
# # Remove
print(library.remove_book("Python Basics"))
library.display_books()

book = library.most_expensive_book()

print(book.display())