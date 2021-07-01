import pytest

from chapter2.linked_lists.delete_middle_node import SolutionDeleteMiddleNode
from commons.linked_list import LinkedList
from test.test_utils.util import equal

delete_middle_node_testcases = [
    # test_list, remove_node, expected_list
    (LinkedList(1, 90, 89, 76, 34, 76), 90, LinkedList(1, 89, 76, 34, 76)),
    (LinkedList(1, 5, 9, 12), 9, LinkedList(1, 5, 12)),
    (LinkedList('a', 'b', 'c', 'd', 'e', 'f'), 'c', LinkedList('a', 'b', 'd', 'e', 'f'))
]


class TestSolutionDeleteMiddleNode:
    solution = SolutionDeleteMiddleNode()

    @pytest.mark.parametrize('test_list, remove_node, expected_list', delete_middle_node_testcases)
    def test_delete_middle_node(self, test_list, remove_node, expected_list):
        self.solution.delete_middle_node(test_list, remove_node)
        assert test_list == expected_list
