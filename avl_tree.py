class AVLNode:
    def __init__(self, isbn, book_data):
        self.isbn = isbn
        self.book_data = book_data  # Stores the full Book object
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, node, isbn, book_data):
        # 1. Standard BST Insert
        if not node:
            return AVLNode(isbn, book_data)
        
        if isbn < node.isbn:
            node.left = self.insert(node.left, isbn, book_data)
        elif isbn > node.isbn:
            node.right = self.insert(node.right, isbn, book_data)
        else:
            return node  # No duplicate ISBNs allowed

        # 2. Update Height
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # 3. Check Balance Factor
        balance = self.get_balance(node)

        # 4. Rotations if unbalanced
        # Left Left Case
        if balance > 1 and isbn < node.left.isbn:
            return self.right_rotate(node)
        # Right Right Case
        if balance < -1 and isbn > node.right.isbn:
            return self.left_rotate(node)
        # Left Right Case
        if balance > 1 and isbn > node.left.isbn:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # Right Left Case
        if balance < -1 and isbn < node.right.isbn:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def search(self, node, isbn):
        if not node or node.isbn == isbn:
            return node
        if isbn < node.isbn:
            return self.search(node.left, isbn)
        return self.search(node.right, isbn)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.book_data)
            self.inorder_traversal(node.right, result)