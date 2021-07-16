'''
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
Hints:#5, #13, #29, #61, #101

https://leetcode.com/problems/palindrome-linked-list/
'''

from commons.linked_list import Node, LinkedList


class SolutionPalindrome:
    def __reverse_and_clone(self, node: Node) -> Node:
        reversed_list = LinkedList()
        while node:
            new_node = Node(node.data)
            new_node.next = reversed_list.head
            reversed_list.head = new_node
            node = node.next

        return reversed_list.head

    def __is_equal(self, node1: Node, node2: Node) -> bool:
        while node1 and node2:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next
        return not node1 and not node2

    def is_palindrome(self, head: Node) -> bool:
        reverse_head = self.__reverse_and_clone(head)
        return self.__is_equal(head, reverse_head)
