import pytest

from ctcl.chapter1.arrays_strings.check_permutation import isvalid_permutation_dicts, isvalid_permutation_bruteforce, \
    isvalid_permutation_optimized

test_data = [
    ('permutation', 'onmueprtati', True),
    ('testing', 'test', False),
    ('Fathom_The_Consequence', 'fathom_the_consequence', False),
    ('Partly', 'PartlyCloudy', False),
    ('master', 'mastermaster', False),
    ('suite', 'sutee', False),
    ('noon', 'noon', True)
]


@pytest.mark.parametrize("word1,word2,expected", test_data)
def test_check_permutation(word1, word2, expected):
    assert expected == isvalid_permutation_dicts(word1, word2)


@pytest.mark.parametrize("word1,word2,expected", test_data)
def test_isvalid_permutation_bruteforce(word1, word2, expected):
    assert isvalid_permutation_bruteforce(word1, word2) == expected


@pytest.mark.parametrize("word1,word2,expected", test_data)
def test_isvalid_permutation_optimized(word1,word2,expected):
    assert isvalid_permutation_optimized(word1,word2) == expected
