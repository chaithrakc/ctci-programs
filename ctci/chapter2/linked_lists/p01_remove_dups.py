'''
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
Hints: #9, #40

Difficulty: Easy
'''
from ctci.commons.linked_list import LinkedList, Node


class SolutionRemoveDups:
    # time complexity O(n) but required extra buffer
    def remove_dups_sets(self, node: Node) -> None:
        unique_node = set()
        prev_node = node
        while node is not None:
            if node.data in unique_node:
                prev_node.next = node.next
            else:
                unique_node.add(node.data)
                prev_node = node
            node = node.next

    # time complexity O(n2) but space optimized
    def remove_dups(self, node: Node) -> None:
        while node is not None:
            runner = node
            while runner.next is not None:
                if runner.next.data == node.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            node = node.next
