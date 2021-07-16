'''
2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129

https://leetcode.com/problems/intersection-of-two-linked-lists/

'''
from commons.linked_list import Node


class SolutionIntersection:
    # using set : O(n+m)
    def get_intersection_node(self, node1: Node, node2: Node) -> Node:
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
