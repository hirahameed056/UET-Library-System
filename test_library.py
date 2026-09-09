import unittest
from library_system import LibrarySystem

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        """Runs before every single test to set up a fresh library."""
        self.lib = LibrarySystem()
        # Add a dummy book: Copies = 2
        self.lib.add_book("111", "Test Book", "Test Author", 2024, "Test", 2)
        self.lib.add_member("M001", "Test Student")

    def test_avl_tree_search(self):
        """Does the AVL tree actually find books by ISBN?"""
        book = self.lib.search_by_isbn("111")
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Test Book")

    def test_hash_table_integration(self):
        """Does the Title Index correctly point to the AVL Tree?"""
        book = self.lib.search_by_title("Test Book")
        self.assertIsNotNone(book)
        self.assertEqual(book.isbn, "111")

    def test_borrowing_logic(self):
        """Can we borrow a book and does stock decrease?"""
        self.lib.borrow_book("M001", "111")
        book = self.lib.search_by_isbn("111")
        self.assertEqual(book.available_copies, 1) # Should drop from 2 to 1

    def test_borrowing_limit(self):
        """Test the 5-book limit rule [cite: 42, 67]"""
        # Add 5 different books
        for i in range(5):
            isbn = f"B00{i}"
            self.lib.add_book(isbn, f"Book {i}", "Author", 2024, "Cat", 5)
            self.lib.borrow_book("M001", isbn)
        
        # Now M001 has 5 books. Try to borrow a 6th one ("111").
        self.lib.borrow_book("M001", "111")
        
        member = self.lib.members.search("M001")
        # Assert that the borrowed count is still 5, not 6
        self.assertEqual(len(member.borrowed_books), 5)

    def test_availability_limit(self):
        """Test that you can't borrow a book with 0 copies [cite: 66]"""
        # Borrow twice (copies were 2)
        self.lib.borrow_book("M001", "111") 
        self.lib.borrow_book("M001", "111") # Now copies = 0 (logic needs to handle duplicate borrows if allowed, but assuming distinct for now or just checking count)
        
        # Add another student to try borrowing the empty book
        self.lib.add_member("M002", "Late Student")
        self.lib.borrow_book("M002", "111")
        
        book = self.lib.search_by_isbn("111")
        # Copies should stay 0, not go to -1
        self.assertEqual(book.available_copies, 0)
        # Student M002 should have 0 books
        member2 = self.lib.members.search("M002")
        self.assertEqual(len(member2.borrowed_books), 0)

if __name__ == '__main__':
    unittest.main()