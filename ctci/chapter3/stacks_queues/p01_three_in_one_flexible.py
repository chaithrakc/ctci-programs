'''
3.1 Three in One: Describe how you could use a single array to implement three stacks.
Hints: #2, #72, #38, #58

Ref - visual explanation of flexible multi stack approach https://www.youtube.com/watch?v=B56kUFIIhQM

'''
from typing import Any

from commons.exceptions import FullStackException, EmptyStackException

'''Allow the stack blocks to be flexible in size. When one stack exceeds its initial capacity, we grow the allowable 
capacity and shift elements as necessary. We will also design our array to be circular, such that the final stack may 
start at the end of the array and wrap around to the beginning '''


class MultiStack:
    class __StackInfo:
        ''' stores metadata about stacks '''

        def __init__(self, start: int, default_size: int):
            self.start = start
            self.capacity = default_size
            self.size = 0

        def isfull(self) -> bool:
            return self.size == self.capacity

        def isempty(self) -> bool:
            return self.size == 0

        def top_index(self) -> int:
            return self.start + self.size - 1

        def last_capacity_index(self) -> int:
            return self.start + self.capacity - 1

    def __init__(self, number_of_stacks: int, default_size: int, params=None):
        self.capacity = default_size * number_of_stacks
        self.data = [None] * (default_size * number_of_stacks)  # max capacity of stack = default size * num of stacks
        self.info = []
        for stack_num in range(number_of_stacks):
            self.info[stack_num] = self.__StackInfo(stack_num * default_size, default_size)
        self.__push_bulk(params)

    def __push_bulk(self, params) -> None:
        if not params:
            return
        for stack_num in params.keys():
            for item in params.get(stack_num):
                self.push(stack_num, item)

    '''1. check if all the stacks are full
            2. if the current stack is full, expand it
            3. increment the size and push the item '''

    def push(self, stack_num: int, item: Any) -> None:
        if self.__all_stack_full():
            raise FullStackException()
        stack_info = self.info[stack_num]
        if stack_info.isfull():
            self.__expand(stack_num)
        stack_info.size = stack_info.size + 1
        self.data[stack_info.top_index()] = item

    def __number_of_items(self):
        total_size = 0
        for stack_info in self.info:
            total_size = total_size + stack_info.size
        return total_size

    def __all_stack_full(self) -> bool:
        return self.capacity == self.__number_of_items()

    def __expand(self, stack_num):
        self.__shift((stack_num + 1) % len(self.info))  # use mod operator to have circular shift
        self.info[stack_num].capacity = self.info[stack_num].capacity + 1

    def __shift(self, stack_num):
        print('//shifting  ', stack_num)
        stack_info = self.info[stack_num]

        # If this stack is at its full capacity, then you need to move the next stack over by one element. This stack
        # can now claim the freed index.
        if stack_info.size >= stack_info.capacity:
            next_stack = (stack_num + 1) % len(self.info)
            self.__shift(next_stack)
            stack_info.capacity = stack_info.capacity + 1  # claim index that next stack lost

        # Shift all elements in stack over by one
        index = stack_info.last_capacity_index()
        while self.__is_within_stack_capacity(stack_info,index):
            self.data[index] = self.data[self.previous_index(index)]
            index = self.previous_index(index)

        # adjust the stack data
        self.data[stack_info.start] = None  # clear the item
        stack_info.start = self.next_index(stack_info.start)  # move the start
        stack_info.capacity = stack_info.capacity - 1  # shrink the capacity

    def adjust_index(self, index) -> int:
        max_capacity = self.capacity
        return ((index % max_capacity) + max_capacity) % max_capacity

    def next_index(self, index) -> int:
        return self.adjust_index(index + 1)

    def previous_index(self, index) -> int:
        return self.adjust_index(index - 1)

    def pop(self, stack_num: int) -> Any:
        stack_info = self.info[stack_num]
        if stack_info.isempty():
            raise EmptyStackException()
        item = self.data[stack_info.top_index()]
        self.data[stack_info.top_index()] = None
        stack_info.size = stack_info.size - 1
        return item

    def peek(self, stack_num: int) -> Any:
        stack_info = self.info[stack_num - 1]
        return self.data[stack_info.top_index()]

    def __is_within_stack_capacity(self, stack_info: __StackInfo, index: int) -> bool:
        if index < 0 or index > self.capacity:
            return False
        contiguous_index = index + self.capacity if index < stack_info.start else index
        end = stack_info.start + self.capacity
        return stack_info.start <= contiguous_index < end

    def __eq__(self, other) -> bool:
        for val1, val2 in zip(self.data, other.data):
            if val1 != val2:
                return False
        return True

    def __hash__(self) -> int:
        return super().__hash__()
