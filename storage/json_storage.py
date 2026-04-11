import json
import os


class JSONStorage:

    def __init__(self, filename):
        self.filename = filename

    def load(self):

        if not os.path.exists(self.filename):
            return {"books": [], "members": []}

        with open(self.filename, "r") as file:
            return json.load(file)

    def save(self, books, members):

        data = {
            "books": [],
            "members": []
        }

        for book in books:
            data["books"].append(book.to_dict())

        for member in members:
            data["members"].append(member.to_dict())

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
