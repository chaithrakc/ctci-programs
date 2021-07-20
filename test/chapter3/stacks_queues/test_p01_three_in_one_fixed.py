from typing import Any

import pytest

from chapter3.stacks_queues.p01_three_in_one_fixed import FixedMultiStack
from commons.exceptions import FullStackException, EmptyStackException

push_tests = [
    (FixedMultiStack(6, {0: [1, 2], 1: [], 2: [1]}), {0: [3], 1: [3], 2: [5]},
     FixedMultiStack(6, {0: [1, 2, 3], 1: [3], 2: [1, 5]})),
    (FixedMultiStack(2, {0: [], 1: [], 2: []}), {0: [3, 4], 1: [3, 4], 2: [3, 4]},
     FixedMultiStack(2, {0: [3, 4], 1: [3, 4], 2: [3, 4]}))
]

empty_tests = [
    (FixedMultiStack(6, {0: [1, 2], 1: [], 2: [1]}), 0, False),
    (FixedMultiStack(6, {0: [1, 2], 1: [], 2: [1]}), 2, False),
    (FixedMultiStack(6, {0: [1, 2], 1: [], 2: [1]}), 1, True),
    (FixedMultiStack(2), 2, True)
]

pop_tests = [
    (FixedMultiStack(6, {0: [1, 2], 1: [], 2: [1]}), 0, FixedMultiStack(6, {0: [1], 1: [], 2: [1]})),
    (FixedMultiStack(6, {0: [1, 2], 1: [], 2: [1]}), 2, FixedMultiStack(6, {0: [1, 2], 1: [], 2: []})),
    (FixedMultiStack(2, {0: [3, 4], 1: [3, 4], 2: [3, 4]}), 1, FixedMultiStack(2, {0: [3, 4], 1: [3], 2: [3, 4]})),
    (FixedMultiStack(2, {0: [3, 4], 1: [3, 4], 2: [3, 4]}), 2, FixedMultiStack(2, {0: [3, 4], 1: [3, 4], 2: [3]}))
]

peek_tests = [
    (FixedMultiStack(6, {0: [1, 2], 1: [], 2: [1]}), 0, 2),
    (FixedMultiStack(6, {0: [1, 2], 1: [], 2: [1]}), 2, 1),
    (FixedMultiStack(2, {0: [3, 4], 1: [3, 4], 2: [3, 4]}), 1, 4),
    (FixedMultiStack(2, {0: ['vendetta', 'subpoena'], 1: ['a', 'b'], 2: ['x', 'y']}), 0, 'subpoena')
]


class TestSolutionThreeInOneFixed:

    @pytest.mark.parametrize('test_stack, items, expected_stack', push_tests)
    def test_push(self, test_stack: FixedMultiStack, items: dict, expected_stack: FixedMultiStack):
        for stack_num, values in items.items():
            for value in values:
                test_stack.push(stack_num, value)
        assert test_stack == expected_stack

    def test_push_fullstack(self):
        with pytest.raises(FullStackException):
            FixedMultiStack(1, {0: [3, 4], 1: [3, 6], 2: [9, 0]})

    @pytest.mark.parametrize('test_stack, stack_num, isempty', empty_tests)
    def test_isempty(self, test_stack: FixedMultiStack, stack_num: int, isempty: bool):
        assert test_stack.isempty(stack_num) is isempty

    @pytest.mark.parametrize('test_stack, stack_num, expected_stack', pop_tests)
    def test_pop(self, test_stack: FixedMultiStack, stack_num: int, expected_stack: FixedMultiStack):
        top_item = test_stack.peek(stack_num)
        removed_item = test_stack.pop(stack_num)
        assert removed_item == top_item and test_stack == expected_stack

    def test_pop_fullstack(self):
        with pytest.raises(EmptyStackException):
            FixedMultiStack(1).pop(2)

    @pytest.mark.parametrize('test_stack, stack_num, expected_elem', peek_tests)
    def test_peek(self, test_stack: FixedMultiStack, stack_num: int, expected_elem: Any):
        top_item = test_stack.peek(stack_num)
        assert top_item == expected_elem

    def test_peek_emptystack(self):
        with pytest.raises(EmptyStackException):
            FixedMultiStack(1).peek(2)
