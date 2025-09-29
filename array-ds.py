# The class shows how static array works
class MyArray:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.data = [None] * size

    # Insert element into array
    def insert(self, data):
        if self.size == self.count:
            raise Exception("Array is full")
        self.data[self.count] = data
        self.count += 1

    # Get trimmed array
    def trimmed_array(self):

        st_array = [] # Initialize empty array to trim the original array
        for element in self.data:
            if element is not None:
                st_array.append(element) # Add the no null element into the array
        return st_array

    # Access array
    def get(self, index = None):
        if index is None:
            print(self.trimmed_array()) # Show the whole array
        else:
            print(self.trimmed_array()[index]) # Show the array by index number
        return

    # Update array element
    def update(self, index, value):
        if  0 <= index <= self.count: # Check the valid index number
            self.data[index] = value # Update the element
            print(self.trimmed_array()) # Return updated array
            return
        else:
            raise Exception("Index number is not valid")

    # Delete array element
    def delete(self, index):
        if 0 <= index <= self.count: # Check the valid index number
            self.data[index] = None # Clear the element
            self.count -= 1
            print(self.trimmed_array()) # Return updated array
            return
        else:
            raise Exception("Index number is not valid")