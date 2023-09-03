# Name: Muritala Olanrewaju
# Student ID: 010882332

class SelfAdjustingHash:
    # Hash table implementation with a time complexity of O(1).
    def __init__(self, size=10, load_factor_threshold=0.75):
        self.size = size * 2  # Double the size on construction
        self.list = [None] * self.size  # Initialize list with None placeholders
        self.load_factor_threshold = load_factor_threshold
        self.item_count = 0  # Keep track of the number of items

    # Insert a key-value pair into the hash table
    def add(self, key, value):
        # Check for resizing
        if self.item_count / self.size >= self.load_factor_threshold:
            self._resize()

        # Make sure the key can be converted to an integer for hashing
        try:
            hashed_key = self._hash_key(key)
        except ValueError:
            print('ERROR: Key must be convertible to an integer.')
            return False

        if self._is_valid_index(hashed_key):
            kvp = [key, value]

            # Check if the index is unoccupied (None)
            if self.list[hashed_key] is None:
                self.list[hashed_key] = kvp
                self.item_count += 1  # Increment the item count
                return True
            else:
                print('ERROR: That package ID already exists.')
                return False
        else:
            print(f'ERROR: Please choose an ID in the range of 0 - {len(self.list) - 1}')
            return False

    # Retrieve a value from the hash table
    def get(self, key):
        hashed_key = self._hash_key(key)
        if self._is_valid_index(hashed_key):
            kvp = self.list[hashed_key]
            if kvp is not None:
                return kvp[1]
        print('ERROR: That package ID does NOT exist.')
        return False

    # Return the hash key
    def _hash_key(self, key):
        return int(key)

    # Validate the index
    def _is_valid_index(self, index):
        return 0 <= index < len(self.list)

    # Resize the hash table
    def _resize(self):
        old_list = self.list
        self.size *= 2  # Double the size
        self.list = [None] * self.size  # Initialize new list with None placeholders
        self.item_count = 0  # Reset item count

        # Rehash all existing items into the new list
        for kvp in old_list:
            if kvp is not None:
                self.add(kvp[0], kvp[1])

    # In your Hash class definition
    def items(self):
        for index in range(self.size):
            kvp = self.list[index]
            if kvp is not None:
                yield kvp[0], kvp[1]  # yield key, value
