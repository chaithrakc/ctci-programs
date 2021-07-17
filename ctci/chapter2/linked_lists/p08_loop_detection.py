'''
2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.

EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C

Hints: #50, #69, #83, #90

Medium Level  https://leetcode.com/problems/linked-list-cycle-ii/
Easy Level https://leetcode.com/problems/linked-list-cycle/

'''
from commons.linked_list import Node


class SolutionLoopDetection:

    # using set()
    def detect_cycle(self, node: Node) -> Node:
        nodes = set()
        while node:
            if node in nodes:
                return node
            nodes.add(node)
            node = node.next
        return None
