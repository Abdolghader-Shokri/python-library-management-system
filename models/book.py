class Book:

    def __init__(self, title, author, year, isbn, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["title"],
            data["author"],
            data["year"],
            data["isbn"],
            data["available"]
        )
