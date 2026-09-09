from library_system import LibrarySystem

def main():
    lib = LibrarySystem()

    # 1. Add Books
    print("--- Adding Books ---")
    lib.add_book("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programming", 3)
    lib.add_book("9780132350884", "Clean Code", "Robert Martin", 2008, "Programming", 5)
    lib.add_book("9780201633610", "Design Patterns", "Erich Gamma", 1994, "Programming", 2)
    lib.add_book("9780132350885", "Clean Architecture", "Robert Martin", 2017, "Programming", 4)

    # 2. Add Members
    print("\n--- Adding Members ---")
    lib.add_member("2024-EE-001", "Ali Khan")
    lib.add_member("2024-EE-002", "Sara Ahmed")

    # 3. Search Examples
    print("\n--- Searching ---")
    print(f"Search by ISBN (9780134685991): {lib.search_by_isbn('9780134685991')}")
    print(f"Search by Title (Clean Code): {lib.search_by_title('Clean Code')}")
    
    print("\nSearch by Author (Robert Martin):")
    robert_books = lib.search_by_author("Robert Martin")
    for b in robert_books:
        print(b)

    # 4. Borrowing
    print("\n--- Borrowing Books ---")
    lib.borrow_book("2024-EE-001", "9780132350884") # Ali borrows Clean Code
    lib.borrow_book("2024-EE-001", "9780134685991") # Ali borrows Effective Python

    # 5. Check Inventory update
    print("\n--- Inventory After Borrowing ---")
    print(lib.search_by_title("Clean Code")) # Copies should be 4

    # 6. Returning
    print("\n--- Returning Books ---")
    lib.return_book("2024-EE-001", "9780132350884")
    print(lib.search_by_title("Clean Code")) # Copies should be back to 5

if __name__ == "__main__":
    main()