'''
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
Hints: #7, #30, #71, #95, #109

https://leetcode.com/problems/add-two-numbers-ii/description/

'''
from commons.linked_list import LinkedList, Node


class SolutionSumListsFollowUp:
    def sum_lists_followup(self, num1_node: Node, num2_node: Node) -> LinkedList:
        num1_node, num2_node = self.__padding_lists(num1_node, num2_node)
        sumlist = LinkedList()
        sumlist.head = Node(0)  # dummy node
        carry = self.__sumlists_helper(num1_node, num2_node, sumlist.head)
        if carry > 0:
            sumlist.head.data = carry  # removing dummy head
        else:
            sumlist.head = sumlist.head.next
        return sumlist

    def __sumlists_helper(self, node1: Node, node2: Node, cur_node: Node) -> int:
        if not node1 and not node2:
            return 0
        cur_node.next = Node(0)  # dummy data
        carry = self.__sumlists_helper(node1.next if node1 else None, node2.next if node2 else None, cur_node.next)
        num1, num2 = node1.data, node2.data
        carry, out = divmod(num1 + num2 + carry, 10)
        cur_node.next.data = out
        return carry

    def __padding_lists(self, node1: Node, node2: Node):
        head1 = node1
        head2 = node2
        while node1 and node2:
            node1 = node1.next
            node2 = node2.next
        head2 = self.__insertbefore(head2, node1)  # pad shorter list2 with zeroes
        head1 = self.__insertbefore(head1, node2)  # pad shorter list1 with zeroes
        return head1, head2

    def __insertbefore(self, head: Node, cur_node: Node):
        while cur_node:
            new_node = Node(0)
            new_node.next = head
            head = new_node
            cur_node = cur_node.next
        return head
