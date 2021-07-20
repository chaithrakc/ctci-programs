from typing import Any

import pytest

from chapter3.stacks_queues.p01_three_in_one_fixed import FixedMultiStack
from commons.exceptions import FullStackException, EmptyStackException

push_tests = [
    (FixedMultiStack(6, {1: [1, 2], 2: [], 3: [1]}), {1: [3], 2: [3], 3: [5]},
     FixedMultiStack(6, {1: [1, 2, 3], 2: [3], 3: [1, 5]})),
    (FixedMultiStack(2, {1: [], 2: [], 3: []}), {1: [3, 4], 2: [3, 4], 3: [3, 4]},
     FixedMultiStack(2, {1: [3, 4], 2: [3, 4], 3: [3, 4]}))
]

empty_tests = [
    (FixedMultiStack(6, {1: [1, 2], 2: [], 3: [1]}), 1, False),
    (FixedMultiStack(6, {1: [1, 2], 2: [], 3: [1]}), 3, False),
    (FixedMultiStack(6, {1: [1, 2], 2: [], 3: [1]}), 2, True),
    (FixedMultiStack(2), 3, True)
]

pop_tests = [
    (FixedMultiStack(6, {1: [1, 2], 2: [], 3: [1]}), 1, FixedMultiStack(6, {1: [1], 2: [], 3: [1]})),
    (FixedMultiStack(6, {1: [1, 2], 2: [], 3: [1]}), 3, FixedMultiStack(6, {1: [1, 2], 2: [], 3: []})),
    (FixedMultiStack(2, {1: [3, 4], 2: [3, 4], 3: [3, 4]}), 2, FixedMultiStack(2, {1: [3, 4], 2: [3], 3: [3, 4]})),
    (FixedMultiStack(2, {1: [3, 4], 2: [3, 4], 3: [3, 4]}), 3, FixedMultiStack(2, {1: [3, 4], 2: [3, 4], 3: [3]}))
]

peek_tests = [
    (FixedMultiStack(6, {1: [1, 2], 2: [], 3: [1]}), 1, 2),
    (FixedMultiStack(6, {1: [1, 2], 2: [], 3: [1]}), 3, 1),
    (FixedMultiStack(2, {1: [3, 4], 2: [3, 4], 3: [3, 4]}), 2, 4),
    (FixedMultiStack(2, {1: ['vendetta', 'subpoena'], 2: ['a', 'b'], 3: ['x', 'y']}), 1, 'subpoena')
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
            FixedMultiStack(1, {1: [3, 4], 2: [3, 6], 3: [9, 0]})

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
            FixedMultiStack(1).pop(3)

    @pytest.mark.parametrize('test_stack, stack_num, expected_elem', peek_tests)
    def test_peek(self, test_stack: FixedMultiStack, stack_num: int, expected_elem: Any):
        top_item = test_stack.peek(stack_num)
        assert top_item == expected_elem

    def test_peek_emptystack(self):
        with pytest.raises(EmptyStackException):
            FixedMultiStack(1).peek(3)
