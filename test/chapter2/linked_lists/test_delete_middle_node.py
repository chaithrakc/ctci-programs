import pytest

from chapter2.linked_lists.delete_middle_node import SolutionDeleteMiddleNode
from test.test_utils.util import get_linkedlist, equal

delete_middle_node_testcases = [
    # test_list, remove_node, expected_list
    ([1, 90, 89, 76, 34, 76], 90, [1, 89, 76, 34, 76]),
    ([1, 5, 9, 12], 9, [1, 5, 12]),
    (['a', 'b', 'c', 'd', 'e', 'f'], 'c', ['a', 'b', 'd', 'e', 'f'])
]


class TestSolutionDeleteMiddleNode:
    solution = SolutionDeleteMiddleNode()

    @pytest.mark.parametrize('test_list, remove_node, expected_list', delete_middle_node_testcases)
    def test_delete_middle_node(self, test_list, remove_node, expected_list):
        linkedlist = get_linkedlist(test_list)
        self.solution.delete_middle_node(linkedlist, remove_node)
        assert equal(linkedlist, expected_list)
