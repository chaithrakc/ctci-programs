'''
3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

Hints:#27, #59, #78

https://leetcode.com/problems/min-stack/
'''
from typing import Any

from commons.exceptions import EmptyStackException


class MinStack:
    def __init__(self, *items):
        self.data = [None] * 50
        self.top = -1
        for item in items:
            self.push(item)

    def push(self, item: Any) -> None:
        self.top = self.top + 1
        self.data[self.top] = item

    def pop(self) -> Any:
        if self.isempty():
            raise EmptyStackException()
        item = self.data[self.top]  # get item
        self.data[self.top] = None  # clear
        self.top = self.top - 1  # update top index
        return item

    def min(self) -> Any:
        if self.isempty():
            raise EmptyStackException()
        return self.data[self.top]

    def isempty(self) -> bool:
        return self.top < 0

    def __eq__(self, other) -> bool:
        for val1, val2 in zip(self.data, other.data):
            if val1 != val2:
                return False
        return True

    def __hash__(self) -> int:
        return super().__hash__()
