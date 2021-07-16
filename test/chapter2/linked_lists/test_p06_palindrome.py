import pytest

from chapter2.linked_lists.p06_palindrome import SolutionPalindrome
from commons.linked_list import LinkedList

palindrome_tests = [
    (LinkedList('m', 'a', 'd', 'a', 'm'), True),
    (LinkedList('r', 'a', 'c', 'e', 'c', 'a', 'r'), True),
    (LinkedList(2, 0, 0, 2), True),
    (LinkedList('step', 'on', 'no', 'pets'), False),
    (LinkedList(90, 76, 100, 100, 76, 90), True),
    (LinkedList(1, 2, 3, 4), False),
    (LinkedList(1, 2, 2, 1), True),
    (LinkedList(0), True)
]


class TestSolutionPalindrome:
    solution = SolutionPalindrome()

    @pytest.mark.parametrize('linkedlist, is_palindrome', palindrome_tests)
    def test_ispalindrome_reverse_compare(self, linkedlist, is_palindrome):
        assert self.solution.ispalindrome_reverse_compare(linkedlist.head) == is_palindrome

    @pytest.mark.parametrize('linkedlist, is_palindrome', palindrome_tests)
    def test_ispalindrome_iterative(self, linkedlist, is_palindrome):
        assert self.solution.ispalindrome_iterative(linkedlist.head) == is_palindrome

    @pytest.mark.parametrize('linkedlist, is_palindrome', palindrome_tests)
    def test_ispalindrome_recursive(self, linkedlist, is_palindrome):
        assert self.solution.ispalindrome_recursive(linkedlist.head) == is_palindrome
