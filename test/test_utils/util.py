from ctci.commons.linked_list import LinkedList, Node


def are_identical_matrices(output_matrix, expected_matrx):
    rows, columns = len(expected_matrx), len(expected_matrx[0])
    for row in range(rows):
        for column in range(columns):
            if output_matrix[row][column] != expected_matrx[row][column]:
                return False
    return True


# compare whether linked list and array are same
def equal(linked_list: LinkedList, array: list) -> bool:
    node = linked_list.head
    index = 0
    while node is not None and index < len(array):
        if node.data != array[index]:
            return False
        node = node.next
        index = index + 1
    return node is None and index == len(array)


# returns linkedlist from an array
def get_linkedlist(array: list) -> LinkedList:
    linked_list = LinkedList()
    if len(array) == 0:
        return linked_list
    node = Node(array[0])
    linked_list.head = node
    for i in range(1, len(array)):
        node.next = Node(array[i])
        node = node.next
    return linked_list
