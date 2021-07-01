'''
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
Hints: #9, #40

Difficulty: Easy
'''
from ctci.commons.linked_list import LinkedList


class SolutionRemoveDups:
    def remove_dups_bruteforce(self, linkedlist: LinkedList) -> None:
        if linkedlist.head is None:
            return
        node = linkedlist.head
        outer_index = 0
        while node is not None:
            temp_node = node.next
            inner_index = outer_index + 1
            while temp_node is not None:
                if node.data == temp_node.data:
                    linkedlist.remove_index(inner_index)
                temp_node = temp_node.next
                inner_index = inner_index + 1
            outer_index = outer_index + 1
            node = node.next
