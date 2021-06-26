import pytest

from ctcl.chapter1.arrays_strings.check_permutation import SolutionPermutation

test_data = [
    ('permutation', 'onmueprtati', True),
    ('testing', 'test', False),
    ('Fathom_The_Consequence', 'fathom_the_consequence', False),
    ('Partly', 'PartlyCloudy', False),
    ('master', 'mastermaster', False),
    ('suite', 'sutee', False),
    ('noon', 'noon', True),
    (' ', ' ', True),
    ('1234', '3421', True)
]


class TestSolutionPermutation:
    __solution = SolutionPermutation()

    @pytest.mark.parametrize('first_word,second_word,expected', test_data)
    def test_isvalid_permutation_dicts(self, first_word, second_word, expected):
        self.__solution.set_input(first_word, second_word)
        assert expected == self.__solution.isvalid_anagram_optimized()

    @pytest.mark.parametrize('first_word,second_word,expected', test_data)
    def test_isvalid_permutation_bruteforce(self, first_word, second_word, expected):
        self.__solution.set_input(first_word, second_word)
        assert self.__solution.isvalid_anagram_bruteforce() == expected

    @pytest.mark.parametrize('first_word,second_word,expected', test_data)
    def test_isvalid_permutation_optimized(self, first_word, second_word, expected):
        self.__solution.set_input(first_word, second_word)
        assert self.__solution.isvalid_anagram_ascii() == expected
