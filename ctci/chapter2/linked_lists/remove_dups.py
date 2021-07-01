'''
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
Hints: #9, #40

Difficulty: Easy
'''
from ctci.commons.linked_list import LinkedList


class SolutionRemoveDups:
    # time complexity O(n) but required extra buffer
    def remove_dups_sets(self, linkedlist: LinkedList) -> None:
        if linkedlist.head is None:
            return
        unique_node = set()
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

    # time complexity O(n2) but space optimized
    def remove_dups(self, linkedlist: LinkedList) -> None:
        if linkedlist.head is None:
            return
        slow_node = linkedlist.head
        while slow_node is not None:
            prev_node = slow_node
            fast_node = slow_node.next
            while fast_node is not None:
                if fast_node.data == slow_node.data:
                    prev_node.next = fast_node.next
                    fast_node = prev_node.next
                    continue
                prev_node = fast_node
                fast_node = fast_node.next
            slow_node = slow_node.next
