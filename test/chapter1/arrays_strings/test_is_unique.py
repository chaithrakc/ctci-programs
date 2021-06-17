import random
import string
import pytest

from ctcl.chapter1.arrays_strings.is_unique import bruteforce, bitvector, ascii_approach


def get_testdata():
    long_str = random.choice(string.ascii_letters) * 130
    return [
        ('Abacus', True),
        ('chaithra', False),
        ('asdfghjkl', True),
        ('123456776', False),
        (long_str, False)
    ]


def get_testdata_bitvector():
    return [
        ('chaithra', False),
        ('asdfghjkl', True),
    ]


failure_message = ' does not have unique letters'


@pytest.mark.parametrize("word,expected", get_testdata())
def test_bruteforce(word, expected):
    assert bruteforce(word) is expected, word + failure_message


@pytest.mark.parametrize("word,expected", get_testdata())
def test_ascii_approach(word, expected):
    assert ascii_approach(word) is expected, word + failure_message


@pytest.mark.parametrize("word,expected", get_testdata_bitvector())
def test_bitvector(word, expected):
    assert bitvector(word) is expected, word + failure_message
