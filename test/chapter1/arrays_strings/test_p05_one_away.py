import pytest

from ctci.chapter1.arrays_strings.p05_one_away import SolutionOneEditAway


def get_testdata():
    test_data = [
        ('pale', 'ple', True),  # remove
        ('ple', 'pale', True),
        ('pales', 'pale', True),  # insertion
        ('pale', 'prr', False),
        ('pale', 'bales', False),
        ('pale', 'bale', True),  # replace
        ('pale', 'bake', False),
        ('format', 'formats', True),  # insertion
        ('format', 'forsmat', True),  # insertion
        ('end', 'end', True),  # zero edits away
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        ("a", "b", True),
        ("pale", "ble", False),
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        ("ale", "elas", False)
    ]
    return test_data


class TestSolutionOneAway:
    __solution = SolutionOneEditAway()

    @pytest.mark.parametrize('first, second, expected', get_testdata())
    def test_one_away(self, first, second, expected):
        self.__solution.set_input(first, second)
        assert self.__solution.one_editaway() == expected
