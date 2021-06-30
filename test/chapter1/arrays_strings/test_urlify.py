import pytest
from ctci.chapter1.arrays_strings.urlify import SolutionURLify


def get_testdata():
    test_data = [
        ('Mr Jhon Smith    ', 13, 'Mr%20Jhon%20Smith'),
        ('Grace Ven Pelt    ', 14, 'Grace%20Ven%20Pelt'),
        ('Mr Patric Jane    ', 14, 'Mr%20Patric%20Jane'),
        ('Red Jhon  ', 8, 'Red%20Jhon'),
        ('Lisbon', 6, 'Lisbon')
    ]
    return test_data


class TestSolutionURLify:
    __solution = SolutionURLify()

    @pytest.mark.parametrize('name,true_length,expected', get_testdata())
    def test_urlify(self, name, true_length, expected):
        self.__solution.set_input(name, true_length)
        assert self.__solution.urlify() == expected
