from typing import Any
import pytest

from chapter3.stacks_queues.p02_stack_min import MinStack

min_tests = [
    (MinStack(1, 2, 3, 4, 0, 5), 1)
]


class TestMinStack:

    @pytest.mark.parametrize('test_stack, min_val', min_tests)
    def test_min(self, test_stack: MinStack, min_val:Any):
        assert test_stack.min() == min_val
