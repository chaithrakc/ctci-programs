import random

from ctcl.commons.linked_list import LinkedList, Node


def get_random_num_list(length: int, num_from: int, num_to: int) -> LinkedList:
    linked_list = LinkedList()
    counter = 0
    node = None
    while counter < length:
        if node is None:
            node = Node(random.randint(num_from, num_to))
            linked_list.head = node
        else:
            node.next = Node(random.randint(num_from, num_to))
            node = node.next
        counter = counter + 1
    return linked_list


class TestLinkedList:

    def test_clear(self):
        get_random_num_list(10, 1, 100)
        assert False

    def test_len(self):
        assert False

    def test_insert(self):
        assert False

    def test_append_head(self):
        assert False

    def test_append_tail(self):
        assert False

    def test_remove(self):
        assert False

    def test_remove_head(self):
        assert False

    def test_remove_tail(self):
        assert False

    def test_find(self):
        assert False
