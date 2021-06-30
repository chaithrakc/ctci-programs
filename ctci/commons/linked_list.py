class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def clear(self) -> None:
        self.head = None

    def len(self) -> int:
        count = 0
        node = self.head
        while node is not None:
            node = node.next
            count = count + 1
        return count

    # index can be at the 0, end, middle, not found - check for all the cases
    def insert(self, index, data) -> bool:
        count = 0
        node = self.head
        prev_node = node
        new_node = Node(data)
        while count <= index and node is not None:
            if count == index:
                prev_node.next = new_node
                new_node.next = node.next
                return True
            prev_node = node
            node = node.next
            count = count + 1
        return False

    def append_head(self, data) -> bool:
        if self.head is None:
            self.head = Node(data)
            return True
        node = self.head
        new_node = Node(data)
        new_node.next = node
        self.head = new_node
        return True

    # need to implement when append can return false
    def append_tail(self, data) -> bool:
        if self.head is None:
            self.head = Node(data)
            return True
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(data)
        return True

    # data can be at the beginning, end, middle, not found - check for all the cases
    def remove(self, data) -> bool:
        if self.head is None:
            return False
        node = self.head
        prev_node = self.head
        while node is not None:
            if node.data == data:
                prev_node.next = node.next
                node.next = None
                return True
            prev_node = node
            node = node.next
        return False

    def remove_head(self) -> bool:
        if self.head is None:
            return False
        node = self.head
        self.head = self.head.next
        node.next = None
        return True

    def remove_tail(self) -> bool:
        if self.head is None:
            return False
        node = self.head
        prev_node = self.head
        while node.next is not None:
            prev_node = node
            node = node.next
        prev_node.next = None
        return True

    def find(self, data) -> int:
        index = 0
        if self.head is None:
            return -1
        node = self.head
        while node is not None:
            if node.data == data:
                return index
            node = node.next
            index = index + 1
        return index

    def __repr__(self):
        node = self.head
        nodes = list()
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
