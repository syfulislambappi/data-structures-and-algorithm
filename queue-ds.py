# The class shows how the queue works

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.popleft()

    def peek(self):
        print(self.queue[0])

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

q1 = Queue()

q1.enqueue("Syful Islam")
q1.enqueue("Bappi Khan")
q1.enqueue("Chowdhury Shaheb")
print(q1.queue)
q1.peek()
q1.dequeue()
print(q1.queue)
q1.peek()
print(q1.is_empty())