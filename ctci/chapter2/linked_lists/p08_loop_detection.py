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

Medium Level https://leetcode.com/problems/linked-list-cycle-ii/
Easy Level https://leetcode.com/problems/linked-list-cycle/

'''
from typing import Optional

from commons.linked_list import Node


class SolutionLoopDetection:

    # using set()
    def detect_cycle(self, node: Node) -> Optional[Node]:
        nodes = set()
        while node:
            if node in nodes:
                return node
            nodes.add(node)
            node = node.next
        return None

    ''' Space Optimized Algorithm Using Runner Technique:
    1. Create two pointers, FastPointer and SlowPointer.
    2. Move FastPointer at a rate of 2 steps and SlowPointer at a rate of 1 step.
    3. When they collide, move SlowPointer to LinkedListHead. Keep FastPointer where it is.
    4. Move SlowPointer and FastPointer at a rate of one step. Return the new collision point
    '''

    def detect_cycle_runner(self, head: Node) -> Optional[Node]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # collision
                break

        # check for no loop
        if not fast or not fast.next:
            return None

        # move slow pointer and fast pointer one step
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
