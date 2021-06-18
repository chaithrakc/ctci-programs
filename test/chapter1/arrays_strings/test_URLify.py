import pytest
from ctcl.chapter1.arrays_strings.URLify import urlify


def get_testdata():
    test_data = [
        ('Mr Jhon Smith    ', 13, 'Mr%20Jhon%20Smith'),
        ('Grace Ven Pelt    ', 14, 'Grace%20Ven%20Pelt'),
        ('Mr Patric Jane    ', 14, 'Mr%20Patric%20Jane'),
        ('Red Jhon  ', 8, 'Red%20Jhon'),
        ('Lisbon', 6, 'Lisbon')
    ]
    return test_data


@pytest.mark.parametrize('string,true_length,expected', get_testdata())
def test_urlify(string, true_length, expected):
    assert urlify(string, true_length) == expected
