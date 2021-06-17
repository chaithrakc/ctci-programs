from ctcl.commons.solution import ISolution
from ctcl.commons.step_input import StepInput
from ctcl.commons.step_output import StepOutput


class Solution(ISolution, ISolution.IBruteForce):
    def __init__(self):
        self.word = None
        self.is_unique = None

    def set_step_input(self, step_input: StepInput):
        self.word = step_input.get_input('word')

    def bruteforce(self):
        for key_index in range(len(self.word)):
            for other_index in range(key_index + 1, len(self.word)):
                if self.word[key_index] == self.word[other_index]:
                    self.is_unique = False
                    return
        self.is_unique = True

    def get_step_output(self):
        step_output = StepOutput()
        step_output.set_output('word', self.is_unique)
        return step_output
