from typing import Any

from commons.exceptions import NoSuchElementException


class QueueNode:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class Queue:
    __first = None
    __last = None

    def __init__(self, *params):
        for item in params:
            self.add(item)

    # Add an item to the end of the queue
    def add(self, item: Any) -> None:
        new_node = QueueNode(item)
        if self.__last:
            self.__last.next = new_node
        self.__last = new_node
        if not self.__first:
            self.__first = new_node

    # Remove the first item in the queue
    def remove(self) -> Any:
        if not self.__first:
            raise NoSuchElementException()
        item = self.__first.data
        self.__first = self.__first.next
        if self.__first is None:  # if queue becomes empty after removing an element
            self.__last = None
        return item

    # Return the top of the queue
    def peek(self) -> Any:
        if not self.__first:
            raise NoSuchElementException()
        return self.__first.data

    # Return true if and only if the queue is empty
    def isempty(self) -> bool:
        return self.__first is None

    def size(self) -> int:
        count = 0
        node = self.__first
        while node:
            count = count + 1
            node = node.next
        return count

    def __repr__(self):
        node = self.__first
        nodes = list()
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return ' -> '.join(nodes)

    def __eq__(self, other) -> bool:
        node1 = self.__first
        node2 = other.__first
        while node1 and node2:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next
        return node1 is None and node2 is None

    def __hash__(self) -> int:
        return super().__hash__()
