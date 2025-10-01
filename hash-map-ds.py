# The class shows how the hashmap work in background

class HashMap:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    # Create hash Unicode
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # Insert data into hashmap
    def __setitem__(self, key, value):
        hashed = self.get_hash(key)
        self.arr[hashed].append((key, value))
        return

    # Get data from the hashmap
    def __getitem__(self, key):
        hashed = self.get_hash(key)

        for text in self.arr[hashed]:
            if text[0] == key:
                print(text[1])
                break
        return

    # Delete data from the hashmap
    def __delitem__(self, key):
        hashed = self.get_hash(key)

        for text in self.arr[hashed]:
           if text[0] == key:
               self.arr[hashed].remove((key, text[1]))

        return

    # Update data from the hashmap
    def update(self, key, value):
        self.__delitem__(key)
        self.__setitem__(key, value)

hash_map = HashMap()
hash_map["march 4"] = "Syful Islam"
hash_map["march 5"] = "Bappi Khan"
hash_map["201"] = "Kutub Ali"
hash_map["102"] = "Nayeem Miya"
hash_map["012"] = "Tamim Miya"
hash_map.update("201", "Abdur Rahman")
hash_map["201"]