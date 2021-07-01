import pytest

from ctci.commons.linked_list import LinkedList
from ctci.chapter2.linked_lists.p01_remove_dups import SolutionRemoveDups


def get_linkedlist_dups():
    return [
        (LinkedList(6, 3, 6, 3, 9, 6, 0, 0, 3, 8), LinkedList(6, 3, 9, 0, 8)),
        (LinkedList(8, 8, 6, 1, 9, 7, 2, 2, 4, 2), LinkedList(8, 6, 1, 9, 7, 2, 4)),
        (LinkedList(1, 7, 2, 0, 2, 1, 3, 2), LinkedList(1, 7, 2, 0, 3)),
        (LinkedList(1, 2, 3, 4, 3, 2, 1), LinkedList(1, 2, 3, 4)),
        (LinkedList(2, 2), LinkedList(2)),
        (LinkedList(), LinkedList()),
        (LinkedList('a'), LinkedList('a')),
        (LinkedList('in', 'abyss', 'finance', 'last', 'append', 'in'), LinkedList('in', 'abyss', 'finance', 'last', 'append')),
        (LinkedList(5.6, 7.9, 8.09, 9.99, 9.999, 8.09), LinkedList(5.6, 7.9, 8.09, 9.99, 9.999))
    ]


class TestSolutionRemoveDups:
    __solution = SolutionRemoveDups()

    @pytest.mark.parametrize('test_list, unique_list', get_linkedlist_dups())
    def test_remove_dups_sets(self, test_list, unique_list):
        self.__solution.remove_dups_sets(test_list.head)
        assert test_list == unique_list

    @pytest.mark.parametrize('test_list, unique_list', get_linkedlist_dups())
    def test_remove_dups(self, test_list, unique_list):
        self.__solution.remove_dups(test_list.head)
        assert test_list == unique_list
