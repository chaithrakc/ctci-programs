import pytest

from ctcl.chapter1.arrays_strings import check_permutation as check_perm

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


@pytest.mark.parametrize('word1,word2,expected', test_data)
def test_isvalid_permutation_dicts(word1, word2, expected):
    assert expected == check_perm.isvalid_anagram_optimized(word1, word2)


@pytest.mark.parametrize('word1,word2,expected', test_data)
def test_isvalid_permutation_bruteforce(word1, word2, expected):
    assert check_perm.isvalid_anagram_bruteforce(word1, word2) == expected


@pytest.mark.parametrize('word1,word2,expected', test_data)
def test_isvalid_permutation_optimized(word1, word2, expected):
    assert check_perm.isvalid_anagram_ascii(word1, word2) == expected
