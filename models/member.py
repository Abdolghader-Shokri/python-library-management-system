class Member:

    def __init__(self, name, member_id, borrowed_books=None):

        self.name = name
        self.member_id = member_id

        if borrowed_books is None:
            self.borrowed_books = []
        else:
            self.borrowed_books = borrowed_books

    def to_dict(self):

        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):

        return Member(
            data["name"],
            data["member_id"],
            data["borrowed_books"]
        )
