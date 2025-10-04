# How binary search tree works
from importlib import reload


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Add data to subtree
    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    # in order traversal
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value):
        if value == self.data:
            return True

        if value < self.data:
            if self.left:
                return  self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

        return 0

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

numbers = [17, 4, 1, 20, 9, 23, 18, 34]

numbers_tree = build_tree(numbers)
print(numbers_tree.delete(20))
print(numbers_tree.in_order_traversal())