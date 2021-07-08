import pytest

from chapter2.linked_lists.p05_sum_lists_followup import SolutionSumListsFollowUp
from commons.linked_list import LinkedList

sum_list_tests_followup = [
    # numlist1 , numlist2, sumlist
    (LinkedList(6, 1, 7), LinkedList(2, 9, 5), LinkedList(9, 1, 2)),
    (LinkedList(3, 8, 7, 9), LinkedList(5, 0, 0), LinkedList(4, 3, 7, 9)),
    (LinkedList(5, 9, 2), LinkedList(7, 6, 9, 9), LinkedList(8, 2, 9, 1)),
    (LinkedList(9, 9, 9), LinkedList(9, 9, 9, 9, 9), LinkedList(1, 0, 0, 9, 9, 8)),
    (LinkedList(9, 7, 8), LinkedList(6, 8, 5), LinkedList(1, 6, 6, 3)),
    (LinkedList(1, 2, 3, 4), LinkedList(5, 6, 7), LinkedList(1, 8, 0, 1)),
    (LinkedList(0), LinkedList(0), LinkedList(0))
]


class TestSolutionSumLists:
    solution = SolutionSumListsFollowUp()

    @pytest.mark.parametrize('numlist1, numlist2, expected_sumlist', sum_list_tests_followup)
    def test_sum_lists_followup(self, numlist1: LinkedList, numlist2: LinkedList, expected_sumlist: LinkedList):
        sumlist = self.solution.sum_lists_followup(numlist1.head, numlist2.head)
        assert sumlist == expected_sumlist

