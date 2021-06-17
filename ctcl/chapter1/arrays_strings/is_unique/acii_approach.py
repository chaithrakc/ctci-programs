from ctcl.commons.solution import ISolution
from ctcl.commons.step_input import StepInput
from ctcl.commons.step_output import StepOutput


class Solution(ISolution, ISolution.ITimeOptimized):
    def __init__(self):
        self.word = None
        self.is_unique = None
        self.NUM_ASCII_CHARS = 128  # assuming character set is ASCII (128 characters)

    def set_step_input(self, step_input: StepInput):
        self.word = step_input.get_input('word')

    def time_optimization(self):
        if len(self.word) > self.NUM_ASCII_CHARS:
            self.is_unique = False
            return
        ascii_histogram = [False] * self.NUM_ASCII_CHARS
        for char in self.word:
            ascii_value = ord(char)
            if ascii_histogram[ascii_value]:
                self.is_unique = False
                return
            ascii_histogram[ascii_value] = True
        self.is_unique = True

    def get_step_output(self):
        step_output = StepOutput()
        step_output.set_output('word', self.is_unique)
        return step_output
