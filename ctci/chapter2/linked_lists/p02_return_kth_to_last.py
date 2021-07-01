'''
2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
Hints:#8, #25, #41, #67, #126

Difficulty: Easy
'''
from ctci.commons.linked_list import Node, LinkedList


class SolutionKthToLast:
    def kth_to_last(self, linkedlist: LinkedList, kth_pos: int):
        runner = linkedlist.head
        node = linkedlist.head
        for count in range(0, kth_pos):
            if runner is None:  # out of bound
                return None
            runner = runner.next
        while runner is not None:
            node = node.next
            runner = runner.next
        return node.data
