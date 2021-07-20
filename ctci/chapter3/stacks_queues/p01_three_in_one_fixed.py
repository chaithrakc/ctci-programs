'''
3.1 Three in One: Describe how you could use a single array to implement three stacks.
Hints: #2, #72, #38, #58
'''
from typing import Any, Optional

from commons.exceptions import EmptyStackException, FullStackException


class FixedMultiStack:
    def __init__(self, stack_capacity: int, params=None):
        self.stack_capacity = stack_capacity
        self.number_of_stacks = 3
        self.data = [None] * (stack_capacity * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
        self.initialize_stack(params)

    # pushing items in bulk
    def initialize_stack(self, params):
        if not params:
            return
        for stack_num in params.keys():
            for item in params.get(stack_num):
                self.push(stack_num, item)

    def push(self, stack_num: int, item: Any) -> None:
        if self.isfull(stack_num):
            raise FullStackException()
        self.sizes[stack_num - 1] = self.sizes[stack_num - 1] + 1  # increase the size
        self.data[self.__index_of_top(stack_num)] = item  # push new item

    def pop(self, stack_num: int) -> Any:
        if self.isempty(stack_num):
            raise EmptyStackException()
        item = self.data[self.__index_of_top(stack_num)]  # Get Top
        self.data[self.__index_of_top(stack_num)] = None  # clear
        self.sizes[stack_num - 1] = self.sizes[stack_num - 1] - 1  # shrink
        return item

    def peek(self, stack_num: int) -> Any:
        if self.isempty(stack_num):
            raise EmptyStackException()
        return self.data[self.__index_of_top(stack_num)]

    def isempty(self, stack_num: int) -> bool:
        return self.sizes[stack_num - 1] == 0

    def __index_of_top(self, stack_num: int) -> int:
        offset = (stack_num - 1) * self.stack_capacity
        size = self.sizes[stack_num - 1] - 1
        return offset + size

    def isfull(self, stack_num):
        return self.sizes[stack_num - 1] == self.stack_capacity

    def __eq__(self, other) -> bool:
        for val1, val2 in zip(self.data, other.data):
            if val1 != val2:
                return False
        return True

    def __hash__(self) -> int:
        return super().__hash__()


