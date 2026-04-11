from models.book import Book
from models.member import Member


class Library:

    def __init__(self, storage):

        self.storage = storage
        self.books = []
        self.members = []

    def load_data(self):

        data = self.storage.load()

        for b in data["books"]:
            self.books.append(Book.from_dict(b))

        for m in data["members"]:
            self.members.append(Member.from_dict(m))

    def save_data(self):

        self.storage.save(self.books, self.members)

    def add_book(self, title, author, year, isbn):

        book = Book(title, author, year, isbn)
        self.books.append(book)

        print("Book added successfully")

    def add_member(self, name, member_id):

        member = Member(name, member_id)
        self.members.append(member)

        print("Member added successfully")

    def find_book(self, isbn):

        for book in self.books:
            if book.isbn == isbn:
                return book

        return None

    def find_member(self, member_id):

        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def borrow_book(self, member_id, isbn):

        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if book is None:
            print("Book not found")
            return

        if member is None:
            print("Member not found")
            return

        if not book.available:
            print("Book is already borrowed")
            return

        book.available = False
        member.borrowed_books.append(isbn)

        print("Book borrowed successfully")

    def return_book(self, member_id, isbn):

        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if book is None or member is None:
            print("Invalid member or book")
            return

        if isbn not in member.borrowed_books:
            print("This member did not borrow this book")
            return

        book.available = True
        member.borrowed_books.remove(isbn)

        print("Book returned successfully")

    def search_by_title(self, title):

        results = []

        for book in self.books:
            if title.lower() in book.title.lower():
                results.append(book)

        return results

    def search_by_author(self, author):

        results = []

        for book in self.books:
            if author.lower() in book.author.lower():
                results.append(book)

        return results
