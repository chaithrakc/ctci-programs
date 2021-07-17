'''
2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129

https://leetcode.com/problems/intersection-of-two-linked-lists/

'''
from typing import Optional

from commons.linked_list import Node


class SolutionIntersection:
    # using set : O(n+m)
    def find_intersection(self, node1: Node, node2: Node) -> Optional[Node]:
        nodes = set()
        while node1:
            nodes.add(node1)
            node1 = node1.next
        while node2:
            if node2 in nodes:
                return node2
            nodes.add(node2)
            node2 = node2.next
        return None

    '''space optimized:
    1. Run through each linked list to get the lengths and the tails.
    2. Compare the tails. If they are different(by reference, not by value),return immediately.There is no intersection.
    3. Set two pointers to the start of each linked list.
    4. On the longer linked list, advance its pointer by the difference in lengths.
    5. Now, traverse on each linked list until the pointers are the same.
    '''

    def find_intersection_iterative(self, node1: Node, node2: Node):
        size1, tail1 = self.__get_length_tailnode(node1)
        size2, tail2 = self.__get_length_tailnode(node2)

        if tail1 != tail2:
            return None  # no intersection

        if size1 > size2:
            node1 = self.__advance_node(node1, size1 - size2)
        elif size2 > size1:
            node2 = self.__advance_node(node2, size2 - size1)

        while node1 and node2 and node1 != node2:
            node1 = node1.next
            node2 = node2.next

        return node1

    def __get_length_tailnode(self, node: Node) -> tuple:
        if node is None:
            return 0, None
        size = 0
        while node.next:
            size = size + 1
            node = node.next
        return size + 1, node

    def __advance_node(self, node: Node, length: int) -> Node:
        for _ in range(length):
            node = node.next
        return node
