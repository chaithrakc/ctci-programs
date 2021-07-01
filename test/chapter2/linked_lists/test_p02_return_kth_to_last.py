import pytest

from ctci.chapter2.linked_lists.p02_return_kth_to_last import SolutionKthToLast
from ctci.commons.linked_list import LinkedList

testcases_kth_to_last = [
    # test_list, kth position, expected_elem
    (LinkedList(), 7, None),
    (LinkedList(1, 2, 3, 4), 4, 1),
    (LinkedList('c', 'a', 'r', 'e', 'e', 'r', 'c', 'u', 'p'), 2, 'u'),
    (LinkedList('agent', 'cho', 'ven', 'pelt', 'grace', 'rigsby'), 3, 'pelt'),
    (LinkedList(0.78, 9.08, 56, 800), 5, None)
]


class TestSolutionKthToLast:
    solution = SolutionKthToLast()

    @pytest.mark.parametrize('test_list, kth_position, exepcted_elem', testcases_kth_to_last)
    def test_kth_to_last(self, test_list, kth_position, exepcted_elem):
        kth_elem = self.solution.kth_to_last(test_list, kth_position)
        assert kth_elem == exepcted_elem
