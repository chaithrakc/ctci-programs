import pytest

from chapter2.linked_lists.p03_delete_middle_node import SolutionDeleteMiddleNode
from commons.linked_list import LinkedList, Node


def get_tests():
    linkedlist1 = LinkedList(1, 90, 89, 76, 34, 100)
    linkedlist2 = LinkedList(1, 5, 9, 12)
    linkedlist3 = LinkedList('a', 'b', 'c', 'd', 'e', 'f')
    linkedlist4 = LinkedList('newyork times', 'economist', 'wall street journal')
    return [
        # test_list, remove_node, expected_list
        (linkedlist1, linkedlist1.head.next, LinkedList(1, 89, 76, 34, 100)),
        (linkedlist2, linkedlist2.head.next.next, LinkedList(1, 5, 12)),
        (linkedlist3, linkedlist3.head.next.next.next, LinkedList('a', 'b', 'c', 'e', 'f')),
        (linkedlist4, None, LinkedList('newyork times', 'economist', 'wall street journal'))
    ]


class TestSolutionDeleteMiddleNode:
    solution = SolutionDeleteMiddleNode()

    @pytest.mark.parametrize('test_list, remove_node, expected_list', get_tests())
    def test_delete_middle_node(self, test_list, remove_node, expected_list):
        self.solution.delete_middle_node(remove_node)
        assert test_list == expected_list
