from ctcl.commons.base_linked_list import ILinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList(ILinkedList):

    def __init__(self):
        self.head = None

    def clear(self) -> None:
        pass

    def len(self) -> int:
        pass

    def insert(self, index, data) -> bool:
        pass

    def append_head(self, data) -> bool:
        pass

    def append_tail(self, data) -> bool:
        pass

    def remove(self, data) -> bool:
        pass

    def remove_head(self):
        pass

    def remove_tail(self):
        pass

    def find(self, data) -> int:
        pass

    def __repr__(self):
        node = self.head
        nodes = list()
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
