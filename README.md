# UET-Library-System
Python library management system using an AVL tree and chained hash tables for catalog indexing, book searches, member management, borrowing, returns, inventory tracking, and automated unit testing.
A Python-based library management system developed as a data structures project at the University of Engineering and Technology Lahore.

The project demonstrates how AVL trees and hash tables can be combined to efficiently organize books, index information, manage members, and process borrowing and returning operations.

## Features

* Add books with ISBN, title, author, publication year, category, and available copies
* Register library members
* Search for books by ISBN
* Search for books by title
* Search for multiple books by author
* Borrow and return books
* Automatically update available copies
* Enforce a maximum borrowing limit of five books per member
* Prevent borrowing when no copies are available
* Test major operations using Python’s `unittest` framework

## Data Structures

| Component      | Data Structure | Purpose                              |
| -------------- | -------------- | ------------------------------------ |
| Book catalogue | AVL tree       | Stores and searches books using ISBN |
| Title index    | Hash table     | Maps normalized book titles to ISBNs |
| Author index   | Hash table     | Maps authors to lists of ISBNs       |
| Member index   | Hash table     | Maps member IDs to member records    |
| Borrowed books | Python list    | Tracks books borrowed by each member |

The AVL tree automatically balances itself using left and right rotations, providing efficient insertion and ISBN searching. The hash tables use separate chaining to handle collisions.

## Project Structure

```text
library-management-system-python/
├── avl_tree.py
├── hash_table.py
├── library_system.py
├── main.py
├── test_library.py
├── README.md
└── .gitignore
```

### `avl_tree.py`

Implements AVL tree nodes, insertion, searching, tree rotations, balance calculation, and in-order traversal.

### `hash_table.py`

Implements a custom hash table with separate chaining. It supports insertion, searching, updating, and deletion.

### `library_system.py`

Contains the main `Book`, `Member`, and `LibrarySystem` classes. It connects the AVL tree and hash-table indexes and implements the library’s main operations.

### `main.py`

Demonstrates adding books and members, searching the catalogue, borrowing books, returning books, and updating inventory.

### `test_library.py`

Contains unit tests for:

* ISBN searching through the AVL tree
* Title searching through the hash-table index
* Borrowing and inventory updates
* The five-book borrowing limit
* Prevention of borrowing unavailable books

## Requirements

* Python 3
* No external packages are required

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/library-management-system-python.git
cd library-management-system-python
```

## Running the Demonstration

```bash
python main.py
```

The demonstration adds sample books and members, performs searches, processes borrowing and returns, and displays inventory changes.

## Running the Tests

```bash
python -m unittest -v test_library.py
```

## Current Limitations

* Information is stored in memory and is cleared when the program closes
* The demonstration uses predefined books and members
* A graphical or interactive command-line interface is not currently included

## Future Improvements

* Add JSON, CSV, or database storage
* Add an interactive command-line interface
* Include book and member deletion
* Develop a graphical or web-based interface

## Author

Hira Hameed
B.Sc. Electrical Engineering
University of Engineering and Technology Lahore
