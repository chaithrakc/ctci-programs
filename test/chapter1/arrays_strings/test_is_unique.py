import random
import string
import pytest

from ctcl.chapter1.arrays_strings.is_unique import SolutionUnique


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


class TestSolutionUnique:
    failure_message = ' does not have unique letters'

    @pytest.mark.parametrize("word,expected", get_testdata())
    def test_bruteforce(self, word, expected):
        solution = SolutionUnique(word)
        assert solution.bruteforce() is expected, word + self.failure_message

    @pytest.mark.parametrize("word,expected", get_testdata())
    def test_ascii_approach(self, word, expected):
        solution = SolutionUnique(word)
        assert solution.ascii_approach() is expected, word + self.failure_message

    @pytest.mark.parametrize("word,expected", get_testdata_bitvector())
    def test_bitvector(self, word, expected):
        solution = SolutionUnique(word)
        assert solution.bitvector() is expected, word + self.failure_message
