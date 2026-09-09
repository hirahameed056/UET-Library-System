class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(self.size)] # Lists for chaining

    def _hash(self, key):
        # Simple hash function: sum of ASCII values % size
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # Check if key exists to update it, otherwise append
        for item in self.table[index]:
            if item[0] == key:
                if isinstance(item[1], list): # For Author index (multiple ISBNs)
                     if value not in item[1]:
                        item[1].append(value)
                else:
                    item[1] = value # Update value
                return
        
        # If key is new
        if isinstance(value, list):
             self.table[index].append([key, value])
        else:
             self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return True
        return False