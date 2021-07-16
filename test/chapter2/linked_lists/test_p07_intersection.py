import pytest

from chapter2.linked_lists.p07_intersection import SolutionIntersection
from commons.linked_list import LinkedList, Node


def get_tests():
    testcase1 = get_intersectionlists(LinkedList('a1', 'a2', 'c1', 'c2', 'c3'), LinkedList('b1', 'b2', 'b3'), 3)
    testcase2 = get_intersectionlists(LinkedList(4, 1, 8, 4, 5), LinkedList(5, 6, 1), 3)
    testcase3 = get_intersectionlists(LinkedList(1, 9, 1, 2, 4), LinkedList(3), 4)
    testcase4 = get_intersectionlists(LinkedList(2, 6, 4), LinkedList(1, 5), 0)
    return [(testcase1[0], testcase1[1], testcase1[2]),
            (testcase2[0], testcase2[1], testcase2[2]),
            (testcase3[0], testcase3[1], testcase3[2]),
            (testcase4[0], testcase4[1], testcase4[2])]


def get_intersectionlists(list1: LinkedList, list2: LinkedList, node_count: int) -> list:
    if not node_count:
        return [list1, list2, 0]
    node1 = list1.head
    node2 = list2.head
    for _ in range(node_count - 1):
        node1 = node1.next
    intersection_node = node1
    while node2.next:
        node2 = node2.next
    node2.next = node1
    return [list1, list2, intersection_node]


class TestSolutionIntersection:
    solution = SolutionIntersection()

    @pytest.mark.parametrize('linkedlist1, linkedlist2, intersecting_node', get_tests())
    def test_get_intersection_node(self, linkedlist1, linkedlist2, intersecting_node):
        node = self.solution.get_intersection_node(linkedlist1.head, linkedlist2.head)
        assert intersecting_node == node
