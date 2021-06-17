import pytest

from ctcl.chapter1.arrays_strings.is_unique.bitvector import Solution
from ctcl.commons.step_input import StepInput
from test.chapter1.arrays_strings.is_unique.data_util import get_testdata_bitvector


@pytest.mark.parametrize("word,is_unique", get_testdata_bitvector())
def test_space_optimization(word,is_unique):
    step_input = StepInput()
    step_input.set_input('word', word)
    solution = Solution()
    solution.set_step_input(step_input)
    solution.space_optimization()
    step_output = solution.get_step_output()
    assert step_output.get_output('word') is is_unique, step_input.get_input('word') + ' does not have unique letters'
