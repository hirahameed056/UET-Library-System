from avl_tree import AVLTree
from hash_table import HashTable

class Book:
    def __init__(self, isbn, title, author, year, category, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.available_copies = int(copies)

    def __str__(self):
        return f"[ISBN: {self.isbn}] {self.title} by {self.author} (Copies: {self.available_copies})"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = [] # List of ISBNs

class LibrarySystem:
    def __init__(self):
        self.book_catalog = AVLTree() # AVL Tree
        self.root = None # Root of AVL Tree
        
        self.title_index = HashTable() # Maps Title -> ISBN
        self.author_index = HashTable() # Maps Author -> List[ISBN]
        self.members = HashTable() # Maps ID -> Member Object

    def add_book(self, isbn, title, author, year, category, copies):
        new_book = Book(isbn, title, author, year, category, copies)
        
        # 1. Insert into AVL Tree
        self.root = self.book_catalog.insert(self.root, isbn, new_book)
        
        # 2. Insert into Title Index (Title -> ISBN)
        # Normalize title: lowercase and strip spaces
        norm_title = title.lower().strip()
        self.title_index.insert(norm_title, isbn)
        
        # 3. Insert into Author Index (Author -> List of ISBNs)
        norm_author = author.lower().strip()
        # Retrieve existing list or create new one is handled in HashTable insert logic modification
        # But for simplicity in our Hash implementation, let's just assume we append strictly
        existing_list = self.author_index.search(norm_author)
        if existing_list is None:
            self.author_index.insert(norm_author, [isbn])
        else:
            if isbn not in existing_list:
                existing_list.append(isbn)

        print(f"Book '{title}' added successfully.")

    def add_member(self, member_id, name):
        new_member = Member(member_id, name)
        self.members.insert(member_id, new_member)
        print(f"Member '{name}' added successfully.")

    def search_by_isbn(self, isbn):
        node = self.book_catalog.search(self.root, isbn)
        if node:
            return node.book_data
        return None

    def search_by_title(self, title):
        # 1. Find ISBN from Hash Table
        isbn = self.title_index.search(title.lower().strip())
        if isbn:
            # 2. Retrieve Book from AVL Tree
            return self.search_by_isbn(isbn)
        return None

    def search_by_author(self, author):
        # 1. Find List of ISBNs from Hash Table
        isbn_list = self.author_index.search(author.lower().strip())
        books = []
        if isbn_list:
            for isbn in isbn_list:
                book = self.search_by_isbn(isbn)
                if book:
                    books.append(book)
        return books

    def borrow_book(self, member_id, isbn):
        member = self.members.search(member_id)
        book_node = self.book_catalog.search(self.root, isbn)

        if not member:
            print("Member not found.")
            return
        if not book_node:
            print("Book not found.")
            return

        book = book_node.book_data

        if book.available_copies > 0 and len(member.borrowed_books) < 5:
            book.available_copies -= 1
            member.borrowed_books.append(isbn)
            print(f"Successfully borrowed '{book.title}'")
        else:
            print("Borrowing failed. Either no copies left or limit reached.")

    def return_book(self, member_id, isbn):
        member = self.members.search(member_id)
        book_node = self.book_catalog.search(self.root, isbn)

        if member and book_node:
            if isbn in member.borrowed_books:
                member.borrowed_books.remove(isbn)
                book_node.book_data.available_copies += 1
                print(f"Returned '{book_node.book_data.title}'")
            else:
                print("Member does not have this book.")