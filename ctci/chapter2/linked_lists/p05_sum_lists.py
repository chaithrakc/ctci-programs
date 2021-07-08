'''
2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

https://leetcode.com/problems/add-two-numbers/

'''

from commons.linked_list import LinkedList, Node


class SolutionSumLists:
    def sum_lists(self, num1_node: Node, num2_node: Node) -> LinkedList:
        sumlist = LinkedList()
        sumlist.head = Node(0)  # Initialize current node to dummy head of the returning list
        sum_node = sumlist.head
        carry = 0
        while num1_node or num2_node:
            num1 = num1_node.data if num1_node else 0
            num2 = num2_node.data if num2_node else 0
            carry, out = divmod(carry + num1 + num2, 10)
            sum_node.next = Node(out)
            sum_node = sum_node.next
            num1_node = num1_node.next if num1_node else None
            num2_node = num2_node.next if num2_node else None
        if carry > 0:
            sum_node.next = Node(carry)
        sumlist.head = sumlist.head.next  # Return dummy head's next node.
        return sumlist