import pytest

from chapter2.linked_lists.p08_loop_detection import SolutionLoopDetection
from commons.linked_list import LinkedList, Node


def get_loop_tests():
    test1 = create_loop(LinkedList('A', 'B', 'C', 'D', 'E'), 2)
    test2 = create_loop(LinkedList(3, 2, 0, -4), 1)
    test3 = create_loop(LinkedList(1, 2), 0)
    test4 = create_loop(LinkedList(1), -1)
    test5 = create_loop(LinkedList(), -1)
    test6 = create_loop(LinkedList(1, 2), -1)
    return [
        (test1[0], test1[1]),
        (test2[0], test2[1]),
        (test3[0], test3[1]),
        (test4[0], test4[1]),
        (test5[0], test5[1]),
        (test6[0], test6[1])
    ]


def create_loop(linkedlist: LinkedList, loop_pos: int) -> tuple:
    if loop_pos < 0 or not linkedlist.head:
        return linkedlist.head, None
    node = linkedlist.head
    while node and loop_pos > 0:
        node = node.next
        loop_pos = loop_pos - 1
    loop_node = node
    while node.next:
        node = node.next
    node.next = loop_node
    return linkedlist.head, loop_node


class TestSolutionLoopDetection:
    solution = SolutionLoopDetection()

    @pytest.mark.parametrize('head, loop_node', get_loop_tests())
    def test_detect_cycle(self, head: Node, loop_node: Node):
        node = self.solution.detect_cycle(head)
        assert node == loop_node

    @pytest.mark.parametrize('head, loop_node', get_loop_tests())
    def test_detect_cycle_runner(self, head: Node, loop_node: Node):
        node = self.solution.detect_cycle_runner(head)
        assert node == loop_node
