import pytest

from ctcl.chapter1.arrays_strings.string_rotation import SolutionStringRotation


def get_testcases():
    return [
        ('waterbottle', 'erbottlewat', True),
        ('recursion','sionrecur',True),
        ('1234','4321', False),
        ('1234','2341', True),
        ('hersheys','heyshers', True),
        ('erererer','rererere', True)
    ]


class TestSolutionStringRotation:
    __solution = SolutionStringRotation()

    @pytest.mark.parametrize('s1,s2,expected', get_testcases())
    def test_valid_rotation(self, s1: str, s2: str, expected: bool):
        self.__solution.set_input(s1, s2)
        assert self.__solution.are_rotated() == expected
