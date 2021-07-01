from commons.linked_list import LinkedList


class SolutionDeleteMiddleNode:
    def delete_middle_node(self, linkedlist:LinkedList, elem):
        node = linkedlist.head
        prev_node = linkedlist.head
        while node is not None:
            if node.data == elem:
                prev_node.next = node.next
                return
            prev_node = node
            node = node.next
