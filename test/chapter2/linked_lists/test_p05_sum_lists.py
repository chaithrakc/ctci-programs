import pytest

from chapter2.linked_lists.p05_sum_lists import SolutionSumLists
from commons.linked_list import LinkedList

sum_list_tests = [
    # numlist1 , numlist2, sumlist
    (LinkedList(7, 1, 6), LinkedList(5, 9, 2), LinkedList(2, 1, 9)),
    (LinkedList(7, 9, 8, 3), LinkedList(0, 0, 5), LinkedList(7, 9, 3, 4)),
    (LinkedList(2, 9, 5), LinkedList(9, 9, 6, 7), LinkedList(1, 9, 2, 8)),
    (LinkedList(9, 9, 9), LinkedList(9, 9, 9, 9, 9), LinkedList(8, 9, 9, 0, 0, 1)),
    (LinkedList(8, 7, 9), LinkedList(5, 8, 6), LinkedList(3, 6, 6, 1)),
    (LinkedList(4, 3, 2, 1), LinkedList(7, 6, 5), LinkedList(1, 0, 8, 1)),
    (LinkedList(0), LinkedList(0), LinkedList(0))
]


class TestSolutionSumLists:
    solution = SolutionSumLists()

    @pytest.mark.parametrize('numlist1, numlist2, expected_sumlist', sum_list_tests)
    def test_sum_lists(self, numlist1: LinkedList, numlist2: LinkedList, expected_sumlist: LinkedList):
        sumlist = self.solution.sum_lists(numlist1.head, numlist2.head)
        assert sumlist == expected_sumlist

    @pytest.mark.parametrize('numlist1, numlist2, expected_sumlist', sum_list_tests)
    def test_sum_lists_recusive(self, numlist1: LinkedList, numlist2: LinkedList, expected_sumlist: LinkedList):
        sumlist = self.solution.sum_lists_recusive(numlist1.head, numlist2.head)
        assert sumlist == expected_sumlist
