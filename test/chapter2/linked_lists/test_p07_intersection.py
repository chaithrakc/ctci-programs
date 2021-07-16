import pytest

from chapter2.linked_lists.p07_intersection import SolutionIntersection
from commons.linked_list import LinkedList, Node


def get_tests():
    testcase1 = get_intersect_lists(LinkedList('a1', 'a2'), LinkedList('b1', 'b2', 'b3'), LinkedList('c1', 'c2', 'c3'))
    testcase2 = get_intersect_lists(LinkedList(4, 1), LinkedList(5, 6, 1), LinkedList(8, 4, 5))
    testcase3 = get_intersect_lists(LinkedList(1, 9, 1), LinkedList(3), LinkedList(2, 4))
    testcase4 = get_intersect_lists(LinkedList(2, 6, 4), LinkedList(1, 5), LinkedList())
    return [(testcase1[0], testcase1[1], testcase1[2]),
            (testcase2[0], testcase2[1], testcase2[2]),
            (testcase3[0], testcase3[1], testcase3[2]),
            (testcase4[0], testcase4[1], testcase4[2])]


def get_intersect_lists(list1: LinkedList, list2: LinkedList, intersect_list: LinkedList) -> list:
    node1 = list1.head
    node2 = list2.head
    while node1.next:
        node1 = node1.next
    while node2.next:
        node2 = node2.next
    node1.next = intersect_list.head
    node2.next = intersect_list.head
    return [list1.head, list2.head, intersect_list.head]


class TestSolutionIntersection:
    solution = SolutionIntersection()

    @pytest.mark.parametrize('head1, head2, intersect_node', get_tests())
    def test_get_intersection_node(self, head1: Node, head2: Node, intersect_node: Node) -> None:
        node = self.solution.get_intersection_node(head1, head2)
        assert intersect_node == node
