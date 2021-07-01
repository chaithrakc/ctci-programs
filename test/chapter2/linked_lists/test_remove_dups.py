import pytest

from ctci.chapter2.linked_lists.remove_dups import SolutionRemoveDups
from test.test_utils.util import get_linkedlist, equal


def get_linkedlist_dups():
    return [
        ([6, 3, 6, 3, 9, 6, 0, 0, 3, 8], [6, 3, 9, 0, 8]),
        ([8, 8, 6, 1, 9, 7, 2, 2, 4, 2], [8, 6, 1, 9, 7, 2, 4]),
        ([1, 7, 2, 0, 2, 1, 3, 2], [1, 7, 2, 0, 3]),
        ([], []),
        (['a'], ['a']),
        (['in', 'abyss', 'finance', 'last', 'append', 'in'], ['in', 'abyss', 'finance', 'last', 'append']),
        ([5.6, 7.9, 8.09, 9.99, 9.999, 8.09], [5.6, 7.9, 8.09, 9.99, 9.999])
    ]


class TestSolutionRemoveDups:
    __solution = SolutionRemoveDups()

    @pytest.mark.parametrize('duplicate_arr, unique_arr',get_linkedlist_dups())
    def test_remove_dups(self, duplicate_arr, unique_arr):
        linkedlist = get_linkedlist(duplicate_arr)
        self.__solution.remove_dups(linkedlist)
        assert equal(linkedlist, unique_arr)
