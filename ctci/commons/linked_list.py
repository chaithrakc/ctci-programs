class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


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

    def insert(self, index, data):
        if self.head is None or index == 0:
            self.append_head(data)
            return
        count = 0
        node = self.head
        prev_node = node
        new_node = Node(data)
        while count <= index and node is not None:
            if count == index:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
            node = node.next
            count = count + 1
        # if index is not found, appending to the end of the list
        prev_node.next = new_node

    def append_head(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = self.head
        new_node = Node(data)
        new_node.next = node
        self.head = new_node

    def append_tail(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(data)

    def remove(self, key_elem) -> int:
        if self.head is None:
            return -1
        if self.head.data == key_elem:
            self.head = self.head.next
            return 0
        index = 0
        node = self.head
        prev_node = self.head
        while node is not None:
            if node.data == key_elem:
                prev_node.next = node.next
                return index
            prev_node = node
            node = node.next
            index = index + 1
        return -1

    def remove_head(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        node.next = None
        return node.data

    def remove_tail(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        node = self.head
        prev_node = self.head
        while node.next is not None:
            prev_node = node
            node = node.next
        prev_node.next = None
        return node.data

    def find(self, key_elem) -> int:
        index = 0
        if self.head is None:
            return -1
        node = self.head
        while node is not None:
            if node.data == key_elem:
                return index
            node = node.next
            index = index + 1
        return -1

    def __repr__(self):
        node = self.head
        nodes = list()
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return ' -> '.join(nodes)
