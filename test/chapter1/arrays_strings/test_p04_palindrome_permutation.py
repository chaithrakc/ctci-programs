import pytest

from ctci.chapter1.arrays_strings.p04_palindrome_permutation import SolutionPalindromePermutation


def get_testdata():
    test_data = [
        ('Tact Coa', True),  # taco cat
        ('Wikipedia', False),
        ('diervriDe', True),  # Redivider
        ('iervrvse', False),  # revivers
        ('reviverst', False),  # revivers
        ('dog am I dogma', True),  # dogma I am god
        ('ielv emit no on emit evil', True)  # Live on time, emit no evil
    ]
    return test_data


class TestSolutionPalindromPermutation:
    __solution = SolutionPalindromePermutation()

    @pytest.mark.parametrize("test_data, expected", get_testdata())
    def test_isvalid_palindrome_permutation(self, test_data, expected):
        self.__solution.set_iput(test_data)
        assert self.__solution.isvalid_palindrome_permutation_dicts() == expected

    @pytest.mark.parametrize("test_data, expected", get_testdata())
    def test_isvalid_palindrome_permutation_bitvector(self, test_data, expected):
        self.__solution.set_iput(test_data)
        assert self.__solution.isvalid_palindrome_permutation_bitvector() == expected
