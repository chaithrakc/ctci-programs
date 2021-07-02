'''
ints:#8, #25, #41, #67, #126
2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
Hints:#72
'''
from ctci.commons.linked_list import Node


class SolutionDeleteMiddleNode:
    def delete_middle_node(self, remove_node: Node):
        if remove_node is None or remove_node.next is None:
            return
        runner = remove_node.next
        remove_node.data = runner.data
        remove_node.next = runner.next
