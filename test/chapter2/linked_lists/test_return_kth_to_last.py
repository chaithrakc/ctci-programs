import pytest

from chapter2.linked_lists.return_kth_to_last import SolutionKthToLast
from test.test_utils.util import get_linkedlist

testcases_kth_to_last = [
    # test_list, kth position, expected_elem
    ([], 7, None),
    ([1, 2, 3, 4], 4, 1),
    (['c', 'a', 'r', 'e', 'e', 'r', 'c', 'u', 'p'], 2, 'u'),
    (['agent', 'cho', 'ven', 'pelt', 'grace', 'rigsby'], 3, 'pelt'),
    ([0.78, 9.08, 56, 800], 5, None)
]


class TestSolutionKthToLast:
    solution = SolutionKthToLast()

    @pytest.mark.parametrize('test_list, kth_position, exepcted_elem', testcases_kth_to_last)
    def test_kth_to_last(self, test_list, kth_position, exepcted_elem):
        linkedlist = get_linkedlist(test_list)
        kth_elem = self.solution.kth_to_last(linkedlist, kth_position)
        assert kth_elem == exepcted_elem
