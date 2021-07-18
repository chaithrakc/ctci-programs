'''
stack implementation using a linked list, if items were added and removed from the same side.
ref : https://rextester.com/discussion/DLSUHP77226/LinkedNode-and-its-use-in-Stack-and-Queue-implementation
'''
from typing import Any

from commons.exceptions import EmptyStackException


class StackNode:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __repr__(self):
        return "StackNode(" + repr(self.data) + "," + repr(self.next) + ")"


class Stack:
    __top = None  # head pointer to stack-linkedlist

    def __init__(self, *items):
        for item in items:
            self.push(item)

    # Remove the top item from the stack
    def pop(self) -> StackNode:
        if not self.__top:
            raise EmptyStackException()
        item = self.__top.data
        self.__top = self.__top.next
        return item

    # Add an item to the top of the stack
    def push(self, item: Any) -> None:
        new_top = StackNode(item)
        new_top.next = self.__top
        self.__top = new_top

    # Return the top of the stack
    def peek(self) -> Any:
        if not self.__top:
            raise EmptyStackException()
        return self.__top.data

    # Return true if and only if the stack is empty.
    def isempty(self) -> bool:
        return self.__top is None

    def size(self) -> int:
        count = 0
        node = self.__top
        while node:
            count = count + 1
            node = node.next
        return count

    def __repr__(self):
        node = self.__top
        nodes = list()
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return ' -> '.join(nodes)

    def __eq__(self, other) -> bool:
        node1 = self.__top
        node2 = other.__top
        while node1 and node2:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next
        return node1 is None and node2 is None

    def __hash__(self) -> int:
        return super().__hash__()
