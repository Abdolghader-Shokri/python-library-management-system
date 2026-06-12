# Library Management System

A command-line **Library Management System** written in Python that allows users to manage books, library members, and borrowing operations.  
This project demonstrates the use of **Object-Oriented Programming (OOP)**, modular project structure, and persistent data storage using JSON.

The application is designed as a small but structured backend-style project that separates data models, business logic, and storage handling into different modules.

## Features

- Add new books to the library
- Register library members
- Borrow books
- Return books
- Search books by title
- Search books by author
- Persistent storage using JSON
- Modular and maintainable project architecture
- Simple command-line interface (CLI)

## How It Works

The program runs through a command-line menu that allows the user to perform different library operations.  
Books and members are managed using Python classes, while the library logic is handled by a dedicated service layer.

All data is stored in a JSON file. When the program starts, the system loads existing data from the file. When the user exits the program, the data is saved again to ensure persistence.

The project structure separates the responsibilities of the system into models, services, and storage layers, which makes the code easier to maintain and extend.

## Project Structure

```
library-management-system/
│
├── models/
│   ├── __init__.py
│   ├── book.py
│   └── member.py
│
├── services/
│   ├── __init__.py
│   └── library.py
│
├── storage/
│   ├── __init__.py
│   └── json_storage.py
│
├── main.py
├── library.json
├── README.md
└── .gitignore
```

- **models/** — contains the data models used in the system  
- **book.py** — defines the `Book` class used to represent books in the library  
- **member.py** — defines the `Member` class used to represent library members  

- **services/** — contains the core business logic of the application  
- **library.py** — manages books, members, borrowing, returning, and searching operations  

- **storage/** — responsible for data persistence  
- **json_storage.py** — handles reading and writing data to the JSON file  

- **main.py** — the main entry point of the application with the CLI interface  
- **library.json** — stores books and members data  
- **README.md** — project documentation  
- **.gitignore** — prevents unnecessary files from being uploaded to GitHub  

## Requirements

- Python 3.x

This project uses only the Python standard library and does not require external packages.

## How to Run

1. Clone the repository

```
git clone https://github.com/Abdolghader-Shokri/python-library-management-system.git
```

2. Navigate to the project directory

```
cd python-library-management-system
```

3. Run the program

```
python main.py
```

## Example Usage

```
Library System

1 Add Book
2 Add Member
3 Borrow Book
4 Return Book
5 Search by Title
6 Search by Author
7 Exit

Choose option: 1
Title: Clean Code
Author: Robert C. Martin
Year: 2008
ISBN: 12345
```

## Learning Goals

This project demonstrates several important Python and software design concepts:

- Object-Oriented Programming (OOP)
- Class design and object modeling
- Separation of concerns
- Modular project architecture
- JSON serialization and deserialization
- File handling in Python
- Command-line interface design

## Future Improvements

Possible enhancements for future versions:

- Add input validation for user data
- Implement logging for system actions
- Add custom exception handling
- Write unit tests for core functionality
- Replace JSON storage with SQLite database
- Build a REST API using Flask or FastAPI
- Create a web interface for the system
