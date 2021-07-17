'''
stack implementation using a linked list, if items were added and removed from the same side.
'''


class Stack:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.top = None  # head pointer to stack-linkedlist

    # Remove the top item from the stack
    def pop(self):
        pass

    # Add an item to the top of the stack
    def push(self, item):
        pass

    # Return the top of the stack
    def peek(self):
        return self.top.data

    # Return true if and only if the stack is empty.
    def isempty(self) -> bool:
        pass

    def __repr__(self):
        pass
