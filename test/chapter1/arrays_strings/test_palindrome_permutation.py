import pytest

from ctcl.chapter1.arrays_strings.palindrome_permutation import isvalid_palindrome_permutation_dicts, \
    isvalid_palindrome_permutation_bitvector


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


@pytest.mark.parametrize("test_data, expected", get_testdata())
def test_isvalid_palindrome_permutation(test_data, expected):
    assert isvalid_palindrome_permutation_dicts(test_data) == expected


@pytest.mark.parametrize("test_data, expected", get_testdata())
def test_isvalid_palindrome_permutation_bitvector(test_data,expected):
    assert isvalid_palindrome_permutation_bitvector(test_data) == expected
