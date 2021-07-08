'''
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
Hints:#5, #13, #29, #61, #101
'''

from commons.linked_list import Node


class SolutionPalindrome:
    def is_palindrome(self, node: Node) -> bool:
        runner = node.next
        temp_arr = list()
        temp_arr.append(node.data)
        while runner and runner.next:
            node = node.next
            runner = runner.next.next
            temp_arr.append(node.data)
        node = node.next
        end_index = len(temp_arr) - 1 if temp_arr[len(temp_arr) - 1] == node.data else len(temp_arr) - 2
        while node and end_index > -1:
            if node.data != temp_arr[end_index]:
                return False
            node = node.next
            end_index = end_index - 1
        return True
