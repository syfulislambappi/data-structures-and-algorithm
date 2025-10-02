# The code shows how the stack works in background with python list

stack = []

stack.append("Syful Islam")
stack.append("Abdur Rahman")
stack.append("Fajle Rabbi")
stack.append("Arman Ahmed")
# print(stack)
# stack.pop()
# print(stack)

# The code shows how the stack works in background with python stack
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def append(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

# stack = Stack()
# stack.append("Syful Islam")
# stack.append("Arman Ahmed")
# print(stack.stack)
# print(stack.stack)

stack = deque(["S", "Y", "B"])
def print_reverse(text):
    stack = deque()
    for t in text:
        stack.append(t)

    data = ""
    for i in range(len(stack)):
        data += stack.pop()

    print(data)
    return

print_reverse("We will conquere COVID-19")