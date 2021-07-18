from typing import Any

import pytest

from commons.exceptions import EmptyStackException
from commons.stack import Stack

push_tests = [
    (Stack(1, 2, 3, 4, 5, 6), 100, Stack(1, 2, 3, 4, 5, 6, 100)),
    (Stack('veritasiam', 'smarter everyday'), '3blue1brown', Stack('veritasiam', 'smarter everyday', '3blue1brown'))
]

pop_tests = [
    (Stack(1, 2, 3, 4, 5, 6), Stack(1, 2, 3, 4, 5)),
    (Stack('veritasiam', 'smarter everyday', '3blue1brown'), Stack('veritasiam', 'smarter everyday'))
]

empty_test = [
    (Stack(), True),
    (Stack('t', 'e', 's', 't'), False)
]

peek_test = [
    (Stack(1, 2, 3, 4, 5, 6), 6),
    (Stack('veritasiam', 'smarter everyday'), 'smarter everyday')
]

size_test = [
    (Stack(1, 2, 3, 4, 5, 6), 6),
    (Stack('veritasiam', 'smarter everyday'), 2),
    (Stack(), 0)
]


class TestStack:

    @pytest.mark.parametrize('test_stack, item, expected_stack', push_tests)
    def test_push(self, test_stack: Stack, item: Any, expected_stack: Stack):
        test_stack.push(item)
        assert test_stack == expected_stack

    @pytest.mark.parametrize('test_stack, peek_item', peek_test)
    def test_peek(self, test_stack: Stack, peek_item):
        assert test_stack.peek() == peek_item

    @pytest.mark.parametrize('test_stack, expected_stack', pop_tests)
    def test_pop(self, test_stack: Stack, expected_stack: Stack):
        top_elem = test_stack.peek()
        removed_item = test_stack.pop()
        assert removed_item == top_elem and test_stack == expected_stack

    @pytest.mark.parametrize('test_stack, isempty', empty_test)
    def test_isempty(self, test_stack: Stack, isempty: bool):
        assert test_stack.isempty() is isempty

    def test_pop_emptystack(self):
        stack = Stack()
        with pytest.raises(EmptyStackException):
            stack.pop()

    def test_peek_emptystack(self):
        stack = Stack()
        with pytest.raises(EmptyStackException):
            stack.peek()

    @pytest.mark.parametrize('test_stack, expected_size', size_test)
    def test_size(self, test_stack: Stack, expected_size: int):
        assert test_stack.size() == expected_size
