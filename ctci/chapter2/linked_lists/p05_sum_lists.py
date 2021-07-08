'''
2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
https://leetcode.com/problems/add-two-numbers/
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
https://leetcode.com/problems/add-two-numbers-ii/description/
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
Hints: #7, #30, #71, #95, #109

'''
from commons.linked_list import LinkedList, Node


class SolutionSumLists:
    def sum_lists(self, numlist1: LinkedList, numlist2: LinkedList) -> LinkedList:
        num1_node = numlist1.head
        num2_node = numlist2.head
        sumlist = LinkedList()
        sumlist.head = Node(0)  # Initialize current node to dummy head of the returning list
        sum_node = sumlist.head
        carry = 0
        while num1_node or num2_node or carry:
            num1 = num1_node.data if num1_node else 0
            num2 = num2_node.data if num2_node else 0
            carry, out = divmod(carry + num1 + num2, 10)
            sum_node.next = Node(out)
            sum_node = sum_node.next
            num1_node = num1_node.next if num1_node else None
            num2_node = num2_node.next if num2_node else None
        sumlist.head = sumlist.head.next  # Return dummy head's next node.
        return sumlist

    def sum_lists_followup(self, numlist1: LinkedList, numlist2: LinkedList) -> LinkedList:
        pass
