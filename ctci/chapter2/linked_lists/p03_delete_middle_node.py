from commons.linked_list import Node


class SolutionDeleteMiddleNode:
    def delete_middle_node(self, remove_node: Node):
        if remove_node is None or remove_node.next is None:
            return
        runner = remove_node.next
        remove_node.data = runner.data
        remove_node.next = runner.next
