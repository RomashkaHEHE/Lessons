from datetime import datetime
from abc import ABC, abstractmethod

class Printable(ABC):
    def print_info():
        pass

class Book(Printable):
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    def info(self):
        return f'"{self.title}" - {self.author}, {self.year} year'
    def print_info(self):
        print(self.info())
    @property
    def age(self):
        return datetime.now().year - self.year
    @age.setter
    def age(self, value):
        self.year = datetime.now().year - value
    def __str__(self):
        return self.info()
    def __eq__(self, other):
        return isinstance(other, Book) and self.info() == other.info()
    @classmethod
    def from_string(cls, content):
        title, author, year = content.split('; ')
        return cls(title, author, int(year))

book123 = Book.from_string('Война и мир; кто-то; 1927')
print(book123) # "Война и мир" - кто-то, 1927 year
print(book123.age) # 98
book123.age = 321
print(book123.age) # 321
print(book123.year) # 1704