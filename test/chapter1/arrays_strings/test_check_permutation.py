import pytest

from ctcl.chapter1.arrays_strings.check_permutation import are_permutations

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
    assert expected == are_permutations(word1,word2)
