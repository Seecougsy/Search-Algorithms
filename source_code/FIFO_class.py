
''' This class holds the queue functionalirty for BFS
    This code is modified (Andrews, 2023)
'''
from collections import deque
class Fifo:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item) # <-- appends items passed


    def dequeue(self):
        return self.items.popleft() #<-- takes item from left of qeue

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)