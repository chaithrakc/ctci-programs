'''
3.1 Three in One: Describe how you could use a single array to implement three stacks.
Hints: #2, #72, #38, #58
'''
from typing import Any

from commons.exceptions import EmptyStackException, FullStackException


class FixedMultiStack:
    NUMBER_OF_STACKS = 3

    def __init__(self, stack_capacity: int, params=None):
        self.stack_capacity = stack_capacity
        self.data = [None] * (stack_capacity * self.NUMBER_OF_STACKS)
        self.sizes = [0] * self.NUMBER_OF_STACKS
        self.__push_bulk(params)

    def __push_bulk(self, items):
        if not items:
            return
        for stack_num in items.keys():
            for item in items.get(stack_num):
                self.push(stack_num, item)

    def push(self, stack_num: int, item: Any) -> None:
        if self.isfull(stack_num):
            raise FullStackException()
        self.sizes[stack_num] = self.sizes[stack_num] + 1  # increase the size
        self.data[self.__get_top_index(stack_num)] = item  # push new item

    def pop(self, stack_num: int) -> Any:
        if self.isempty(stack_num):
            raise EmptyStackException()
        item = self.data[self.__get_top_index(stack_num)]  # Get Top
        self.data[self.__get_top_index(stack_num)] = None  # clear
        self.sizes[stack_num] = self.sizes[stack_num] - 1  # shrink
        return item

    def peek(self, stack_num: int) -> Any:
        if self.isempty(stack_num):
            raise EmptyStackException()
        return self.data[self.__get_top_index(stack_num)]

    def isempty(self, stack_num: int) -> bool:
        return self.sizes[stack_num] == 0

    def __get_top_index(self, stack_num: int) -> int:
        offset = stack_num * self.stack_capacity
        size = self.sizes[stack_num] - 1
        return offset + size

    def isfull(self, stack_num):
        return self.sizes[stack_num] == self.stack_capacity

    def __eq__(self, other) -> bool:
        for val1, val2 in zip(self.data, other.data):
            if val1 != val2:
                return False
        return True

    def __hash__(self) -> int:
        return super().__hash__()
