from ctcl.commons.linked_list import LinkedList, Node


class TestSolutionRemoveDups:
    def test_remove_dups(self):
        linked_list = LinkedList(Node(12))
        linked_list.head.next = Node(20)
        linked_list.head.next.next = Node(34)
        print(linked_list.__repr__())
        assert False
