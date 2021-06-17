"""We can reduce our space usage by a factor of eight by using a bit vector. We will assume, in the below code,
    that the string only uses the lowercase letters a through z. This will allow us to use just a single int."""

from ctcl.commons.solution import ISolution
from ctcl.commons.step_input import StepInput
from ctcl.commons.step_output import StepOutput


class Solution(ISolution, ISolution.ISpaceOptimized):
    def __init__(self):
        self.word = None
        self.is_unique = None

    def set_step_input(self, step_input: StepInput):
        self.word = step_input.get_input('word')

    def space_optimization(self):
        checker = 0
        for char in self.word:
            bit_index = ord(char) - ord('a')
            if checker & (1 << bit_index) > 0:
                self.is_unique = False
                return
            checker = checker | (1 << bit_index)
        self.is_unique = True

    def get_step_output(self):
        step_output = StepOutput()
        step_output.set_output('word', self.is_unique)
        return step_output


'''
With the checker integer, each bit corresponds to a letter in the alphabet. 
The bit at position 0 corresponds to a, position 1 to b, 2 to c, and so on. 
The state of the bit (0 or 1) indicates if the corresponding character has been found in the string.
This method goes through each character in the string. It will set the corresponding bit to 1; 
but first it will check if the bit is already set to 1. If it is, then that means that the character has been seen before.

#converts the character to a bit index. a->0, b->1, etc
            bit_index = ord(char) - ord('a')  # This limits to verifying uniqueness with lower case letters
             bit_index = ord(char)  # not space optimized but overcomes the limitaion of lowe case letters

#checks if the bit is already set. (1 << val) is the bitmask.
            if checker & (1 << bit_index) > 0:   

# sets the appropriate bit.
            checker = checker | (1 << bit_index)  
'''
