import pytest

from ctcl.chapter1.arrays_strings.string_compresser import SolutionCompresser


def get_testcases():
    test_cases = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcd', 'abcd'),
        ('ABCDDE', 'ABCDDE'),
        ('aaaaaaBccDZZ', 'a6B1c2D1Z2'),
        ('a', 'a')
    ]
    return test_cases


class TestSolutionCompresser:
    __solution = SolutionCompresser()

    @pytest.mark.parametrize('decompressed, compressed', get_testcases())
    def test_compresser_iteration(self, decompressed, compressed):
        self.__solution.set_input(decompressed)
        assert self.__solution.compresser_bruteforce() == compressed
