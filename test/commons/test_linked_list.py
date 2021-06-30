import pytest

from ctci.commons.linked_list import Node, LinkedList


def get_test_arrays():
    return [
        ([1, 2, 3, 4, 5, 6]),
        (['test_str']),
        ([]),
        ([56, 89, 100]),
        (['c', 's', 'u', 'n', 'n', 'y'])
    ]


class TestLinkedList:

    def get_linkedlist(self, array: list) -> LinkedList:
        linked_list = LinkedList()
        if len(array) == 0:
            return linked_list
        node = Node(array[0])
        linked_list.head = node
        for i in range(1, len(array)):
            node.next = Node(array[i])
            node = node.next
        return linked_list

    @pytest.mark.parametrize('array', get_test_arrays())
    def test_clear(self, array):
        linked_list = self.get_linkedlist(array)
        linked_list.clear()
        assert linked_list.head is None

    @pytest.mark.parametrize('array', get_test_arrays())
    def test_len(self, array):
        linked_list = self.get_linkedlist(array)
        assert linked_list.len() == len(array)

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
