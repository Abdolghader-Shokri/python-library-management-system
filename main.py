from services.library import Library
from storage.json_storage import JSONStorage


def main():

    storage = JSONStorage("library.json")
    library = Library(storage)

    library.load_data()

    while True:

        print("\nLibrary System")
        print("1 Add Book")
        print("2 Add Member")
        print("3 Borrow Book")
        print("4 Return Book")
        print("5 Search by Title")
        print("6 Search by Author")
        print("7 Exit")

        choice = input("Select option: ")

        if choice == "1":

            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            isbn = input("ISBN: ")

            library.add_book(title, author, year, isbn)

        elif choice == "2":

            name = input("Name: ")
            member_id = input("Member ID: ")

            library.add_member(name, member_id)

        elif choice == "3":

            member_id = input("Member ID: ")
            isbn = input("ISBN: ")

            library.borrow_book(member_id, isbn)

        elif choice == "4":

            member_id = input("Member ID: ")
            isbn = input("ISBN: ")

            library.return_book(member_id, isbn)

        elif choice == "5":

            title = input("Enter title: ")

            results = library.search_by_title(title)

            for book in results:
                print(book.title, "-", book.author)

        elif choice == "6":

            author = input("Enter author: ")

            results = library.search_by_author(author)

            for book in results:
                print(book.title, "-", book.author)

        elif choice == "7":

            library.save_data()
            print("Data saved")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
