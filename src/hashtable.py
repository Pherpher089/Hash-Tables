# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'LinkedPair: {self.key}, {self.value}'


class HashTable:
    def __repr__(self):
        return f'{self.storage}'

    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.count = 0
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        if self.storage[idx] != None:
            if self.storage[idx].key == key:
                pass  # over write
            else:
                # search the list of collisions
                next_node = self.storage[idx]
                while next_node != None:
                    if next_node.next == None:
                        next_node.next = LinkedPair(key, value)
                        next_node = None
                    else:
                        next_node = next_node.next
        else:
            # assign value to index
            self.storage[idx] = LinkedPair(key, value)
            self.count += 1
            if self.count == self.capacity:
                self.resize()

        return value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        node = LinkedPair(None, None)
        node.next = self.storage[idx]
        while node.next != None:
            if node.next.key == key:
                node.next = node.next.next
                return
            else:
                node = node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        node = LinkedPair(None, None)
        node.next = self.storage[idx]
        while node.next != None:
            if node.next.key == key:
                return node.next.value
            else:
                node.next = node.next.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #!!!!!!!
        # Resize method not coppying collisions
        double_cap = self.capacity * 2
        new_arr = [None] * double_cap
        for i in range(self.capacity):
            if self.storage[i] != None:
                new_arr[self._hash_mod(self.storage[i].key)] = self.storage[i]
        self.storage = new_arr
        self.capacity = double_cap


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
