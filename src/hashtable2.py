# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f"<{self.value}>"

class HashTable:
    
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
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
        return self._hash(key) % self.capacity

    
    def insert(self, key, value):
        index = self._hash_mod(key)
        pair = self.storage[index]
        if pair is not None:
            print("overrirde")
            pair.key = key
            pair.value = value
        else:
            self.storage[index] = LinkedPair(key, value)
        # index = self._hash_mod(key)
        # lp = LinkedPair(key, value)

        # lp.next = self.storage[index]
        # self.storage[index] = lp

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None and self.storage[index].key == key:
            return self.storage[index].value
        else:
            print("something went wrong")
        # index = self._hash_mod(key)
        # lp = self.storage[index]
        # if lp:
        #     prev = None

        #     while True:
        #         if lp.key == key:
        #             if prev:
        #                 prev.next = lp.next
        #                 lp = None
        #                 break
        #             elif self.storage[index].next:
        #                 self.storage[index] = None
        #                 break
        #             else:
        #                 self.storage[index] = None
        #                 break
        #         else:
        #             if lp.next == None:
        #                 break
        # else:
        #     print("key not found!")  

    def retrieve(self, key):
        index = self._hash_mod(key)
        lp = self.storage[index]

        if lp:
            while True:
                if lp.key == key:
                    return lp.value
                else:
                    if lp.next:
                        lp = lp.next
                    else:
                        return None
        else:
            return None
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        old_storage = self.storage
        self.storage = new_storage
        
        for i in old_storage:
            if i:
                self.insert(i.key, i.value)
                lp = i
                while lp.next:
                    lp = lp.next
                    self.insert(lp.key, lp.value)


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