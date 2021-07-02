from commons.linked_list import LinkedList, Node


class SolutionSumLists:
    def sum_lists(self, numlist1: LinkedList, numlist2: LinkedList) -> LinkedList:
        num1_node = numlist1.head
        num2_node = numlist2.head
        sumlist = LinkedList()
        carry_over = 0
        while num1_node is not None and num2_node is not None:
            total = carry_over + num1_node.data + num2_node.data
            sum_digit = total % 10  # last digit of the total
            carry_over = total // 10
            sumlist.append_tail(sum_digit)
            num1_node = num1_node.next
            num2_node = num2_node.next
        if num1_node is not None:
            self.sum_lists_helper(sumlist, carry_over, num1_node)
        elif num2_node is not None:
            self.sum_lists_helper(sumlist, carry_over, num2_node)
        elif carry_over > 0:
            sumlist.append_tail(carry_over)

        return sumlist

    def sum_lists_helper(self, sumlist: LinkedList, carry_over: int, node: Node):
        while node is not None:
            total = carry_over + node.data
            sum_digit = total % 10  # last digit of the total
            carry_over = total // 10
            sumlist.append_tail(sum_digit)
            node = node.next
        if carry_over > 0:
            sumlist.append_tail(carry_over)
