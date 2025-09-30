# The class shows how the single linked list works
from operator import index


# Create the Node of LinkedList
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Create LinkedList functionalities
class LinkedList:
    def __init__(self):
        self.head = None # Empty LinkedList

    # Store node at the begining
    def prepend(self, data):
        node = Node(data) # Create node for LinkedList
        node.next = self.head # Store previous Nodes if available or empty as references in the next
        self.head = node # Store the new node to the LinkedList

    # Store node at the ending
    def append(self, data):
        node = Node(data) # Create node for LinkedList
        if self.head is None: # Check if the LinkedList is empty
            self.head = node # Store the node to empty Linkedlist
        last = self.head # Store the Existing Linkedlist
        while last.next: # Traverse till last node
            last = last.next

        last.next = node # Store the node to the last node of next

    # Create LinkedList from the array of elements
    def insert_values(self, values):
        for value in values:
            self.append(value)

    # Get length of the LinkedList
    def length(self):
        count = 0
        last = self.head
        while last:
            last = last.next
            count += 1
        print(count)
        return

    # Remove Node of a LinkedList with given index
    def remove_at(self, index):

        # Check the validity of index number
        if 0 > index >= self.length():
            raise  Exception("Invalid index number")

        temp = self.head
        # If index is 0 it can remove the node
        if index == 0:
            self.head= temp.next
            temp = None
            return

        # Delete node while index is greater than 0
        count = 0
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1

    # Insert node at specific location
    def insert_at(self, index, data):
        if 0 > index >= self.length():
            raise Exception("Invalid index number")

        if index == 0:
            self.prepend(data)

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                node = Node(data)
                node.next = temp.next
                temp.next = node
                break
            temp = temp.next
            count += 1

    # Print the element of LinkedList
    def print(self):
        llstr = "" # empty string to store the element of LinkedList from the node
        last = self.head # Store the LinkedList
        while last: # Check while self.head is true
            llstr += str(last.data) + "-->" # Append the element from node
            last = last.next # Assign the next node to the last variable
        print(llstr)