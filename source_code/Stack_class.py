# Get path code based on (Andrews, 2023)
class Stack:

    # constructor method
    def __init__(self):
        self.items = []

    # check if stack is empty
    def is_empty(self):
        return not self.items #<-- so as not to return bool

    # add items to the list
    def push(self, item):
        self.items.append(item)

    # removes the last item and returns the value
    def pop(self):
        return self.items.pop()

    # shows list item in list
    def peek(self):
        return self.items[-1]

    # size of list
    def size(self):
        return len(self.items)

    def fifo_pop(self):
        return self.items.pop(0)

    # turns obj into string
    def __str__(self):
        return str(self.items)
