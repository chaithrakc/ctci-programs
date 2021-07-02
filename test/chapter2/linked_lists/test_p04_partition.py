import pytest

from chapter2.linked_lists.p04_partition import SolutionPartition
from commons.linked_list import LinkedList

partition_tests = [
    (LinkedList(3, 5, 8, 5, 10, 2, 1), 5),
    (LinkedList(10, 8, 8, 5, 10, 2, 1), 5),
    (LinkedList(90, 76, 23, 17, 10, 7, 6, 0), 0),
    (LinkedList(8, 9, 10, 7, 4, 5, 6), 7),
    (LinkedList(), 10),
    (LinkedList('s', 'c', 'o', 'r', 'p', 'i', 'o', 's'), 'o'),
    (LinkedList(1, 4, 5, 89, 90, 500), 500)
]


class TestSolutionPartition:
    solution = SolutionPartition()

    @pytest.mark.parametrize('test_list, pivot', partition_tests)
    def test_partition(self, test_list, pivot):
        self.solution.partition(test_list, pivot)
        assert self.isvalid_partition(test_list, pivot)

    def isvalid_partition(self, test_list: LinkedList, pivot) -> bool:
        node = test_list.head
        # checking for values less than pivot
        while node is not None:
            if node.data >= pivot:
                break
            node = node.next
        # checking for values greater than pivot
        while node is not None:
            if node.data < pivot:
                return False
            node = node.next
        return True
