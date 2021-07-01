'''
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
Hints: #9, #40

Difficulty: Easy
'''
from ctci.commons.linked_list import LinkedList


class SolutionRemoveDups:
    # time complexity O(n)
    def remove_dups_sets(self, linkedlist: LinkedList) -> None:
        unique_node = set()
        if linkedlist.head is None:
            return
        node = linkedlist.head
        prev_node = linkedlist.head
        while node is not None:
            if node.data in unique_node:
                prev_node.next = node.next
                node = prev_node.next
                continue
            unique_node.add(node.data)
            prev_node = node
            node = node.next
