from ctcl.chapter1.arrays_strings.is_unique.bruteforce_approach import Solution
from ctcl.commons.step_input import StepInput


def test_bruteforce():
    step_input = StepInput()
    step_input.set_input('word', 'chaithra')
    solution = Solution()
    solution.set_step_input(step_input)
    solution.bruteforce()
    step_output = solution.get_step_output()
    assert step_output.get_output('word') is False, step_input.get_input('word') + ' does not have unique letters'

