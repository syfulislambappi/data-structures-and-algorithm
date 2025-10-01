# The classes show how the single linked list works


# Create Single LinkedList Node
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the beginning
    def prepend(self, data):
        new_node = Node(data) # Create new node
        new_node.next = self.head # Store the reference of next node to the present node
        self.head = new_node # Insert node at the beginning
        return

    # Insert at the end
    def append(self, data):
        temp = self.head

        # If LinkedList is empty store the data at the beginning
        if temp is None:
            self.prepend(data)

        # Traverse through to last next pointer
        while temp.next:
            temp = temp.next

        temp.next = Node(data) # Store node to the last next pointer
        return

    # Insert at specific index
    def insert(self, i, data):
        temp = self.head # Store LinkedList for modification

        # Check the validity of index number
        if 0 > i > self.length():
            raise Exception("Invalid index number")

        # Traverse through temp list to insert at specific index
        count = 0
        while temp:
            if i == 0:
                self.prepend(data)
                break
            if count == i - 1:
                new_node = Node(data) # Create new node
                new_node.next = temp.next # Store reference to the rest of the node to the new node
                temp.next = new_node # Store new node at the specified index
                break

            temp = temp.next
            count += 1

        return

    # Insert after value
    def insert_after(self, text, data):
        temp = self.head

        while temp:
            if temp.data == text:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                break

            temp = temp.next

        return

    # Update at specific index
    def update(self, i, data):
        temp = self.head

        # Check the validity of index
        if 0 > i > self.length():
            raise Exception("Invalid index number")

        # Update the data
        count = 0
        while temp:
            if count == i:
                temp.data = data
                break
            temp = temp.next
            count += 1

        return

    # Delete at beginning
    def remove_first(self):
        temp = self.head

        # Remove first item
        while temp:
            temp = temp.next
            break
        self.head = temp

        return

    # Delete at ending
    def remove_last(self):
        temp = self.head

        # Remove from the last index
        while temp:
            if temp.next.next is None:
                temp.next = temp.next.next
                break
            temp = temp.next

        return

    # Delete at specific index
    def remove(self, i):
        temp = self.head
        if 0 > i > self.length():
            raise Exception("Invalid index")

        if i == 0:
            self.remove_first()

        count = 0
        while temp:
            if count == i - 1:
                temp.next = temp.next.next

            temp = temp.next
            count += 1

        return

    # Delete by value
    def remove_by_value(self, key):
        temp = self.head

        while temp:
            if temp.next.data == key:
                temp.next = temp.next.next
                break
            temp = temp.next

        return

    # Get the length of LinkedList
    def length(self):
        count = 0

        while self.head:
            self.head = self.head.next
            count += 1

        return count

    # Print Linkedlist data
    def print(self):
        temp = self.head # Store LinkedList into the temporary variable

        # Show the message if LinkedList is empty
        if temp is None:
            print("LinkedList is empty")

        # Traverse through the LinkedList
        while temp:
            print(temp.data + "-->", end="")
            temp = temp.next
        print()

        return

# linkedList = SingleLinkedList()
# linkedList.prepend("Syful Islam")
# linkedList.prepend("Abdur Rahman")
# linkedList.prepend("Nayeem Islam")
# linkedList.append("Raisul Juhala")
# linkedList.insert(1, "Bappi Khan")
# linkedList.print()
# linkedList.insert_after("Bappi Khan", "Taifur Rahman")
# linkedList.print()
# linkedList.remove_by_value("Abdur Rahman")
# linkedList.print()

# Create Double LinkedList Node
class Nodes:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insert at beginning
    def prepend(self, data):
        node = Nodes(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        return

    # Insert at the ending
    def append(self, data):
        node = Nodes(data)

        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            node.prev = temp

        return
    # Print forward data
    def print_fd(self):
        temp = self.head

        while temp:
            print(temp.data + "-->", end="")
            temp = temp.next

        print()
        return

    # Print backward data
    def print_bd(self):
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data + "-->", end="")
            temp = temp.prev

        print()
        return

dblinkedlist = DoubleLinkedList()
dblinkedlist.prepend("DU")
dblinkedlist.prepend("RU")
dblinkedlist.prepend("CU")
dblinkedlist.print_fd()
dblinkedlist.append("JU")
dblinkedlist.print_fd()
dblinkedlist.print_bd()