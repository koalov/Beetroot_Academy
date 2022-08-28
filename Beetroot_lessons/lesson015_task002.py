"""Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class
and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the
specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified
year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all
existing books

class Library:
    pass

class Book:
    pass

class Author:
    pass
"""


class Author:
    """Every Author instance should contain author's name, country, birthday.
    Additionally, it should contain information about the books, his wrote."""

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books_names = []

    def __repr__(self):
        return f'Author: {self.name}, was born in {self.country} at ' \
               f'{self.birthday} \nhas wrote book(s) {self.books_names}'

    def __str__(self):
        return f'Author: {self.name}, was born in {self.country} at ' \
               f'{self.birthday} \nhas wrote book(s) {self.books_names}'


class Book:
    quantity = 0
    books = []

    def __init__(self, name: str):
        self.name = name
        Book.books = Library.get_books

    def __repr__(self):
        return f'<Book: "{self.name}" has been written in ' \
               f'{self.__dict__.get("year")} by ' \
               f'{self.__dict__.get("author")}>'

    def __str__(self):
        return f'<Book: "{self.name}" has been written in ' \
               f'{self.__dict__.get("year")} by ' \
               f'{self.__dict__.get("author")}>'


class Library:

    def __init__(self, name):
        self.name = name
        self.book = Book
        self.books = []

    def new_books(self, book, name: str, year: int, author: Author):
        """Returns an instance of Book class and adds the book to the books list for
        the current library."""
        self.book = book
        self.book.name = name
        self.book.year = year
        self.book.author = author.name
        self.books.append(self.book)
        Book.quantity += 1
        self.__get_book_name(self.book.name, author)

    def group_by_author(self, author: Author):
        """Returns a list of all books grouped by the specified author"""
        for book in self.books:
            if book.author == author.name:
                print(book)

    def group_by_year(self, year: int):
        """Returns a list of all the books grouped by the specified year"""
        for book in self.books:
            if int(book.year) == year:
                print(book)

    def __get_book_name(self, book, author):
        author.books_names.append(book)

    def get_books(self):
        return self.books

    def __repr__(self):
        return f'Library({self.name}, books: {[book.name for book in self.books]})'

    def __str__(self):
        return f'Library({self.name}, books: {[book.name for book in self.books]})'


lib = Library('Archive 1')
author1 = Author("Mark Lutz", "Switzerland", "01 March 1941")
author2 = Author("Marcel Proust", "France", "10 July 1871")
author3 = Author("James Joyce", "Ireland", "02 February 1882")
author4 = Author("Miguel de Cervantes", "Spain", "29 September 1547")
book1 = Book("Learning Python")
lib.new_books(book1, "Learning Python", 2011, author1)
book2 = Book("In Search of Lost Time")
lib.new_books(book2, "In Search of Lost Time", 1913, author2)
book3 = Book("Ulysses")
lib.new_books(book3, "Ulysses", 1920, author3)
book4 = Book("Don Quixote")
lib.new_books(book4, "Don Quixote", 1615, author4)
book5 = Book("Galatea")
lib.new_books(book5, "Galatea", 1612, author4)
print(repr(lib))
print(repr(book4))
print(repr(author4))
lib.group_by_author(author4)
lib.group_by_year(2011)
print(Book.quantity)