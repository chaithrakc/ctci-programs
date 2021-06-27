import pytest

from ctcl.chapter1.arrays_strings.zero_matrix import SolutionZeroMatrix
from test.chapter1.arrays_strings.test_utils.util import are_identical_matrices


def get_testdata():
    return [
        ([[1, 2, 0], [3, 4, 5], [6, 7, 8]],
         [[0, 0, 0], [3, 4, 0], [6, 7, 0]]),
        ([[1], [2], [0]],
         [[0], [0], [0]]),
        ([[1, 0, 3]], [[0, 0, 0]]),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 0, 23, 24]],
         [[1, 2, 0, 4, 5], [6, 7, 0, 9, 10], [11, 12, 0, 14, 15], [16, 17, 0, 19, 20], [0, 0, 0, 0, 0]]),
        ([[1, 2, 3], [4, 0, 5], [0, 7, 8]],
         [[0, 0, 3], [0, 0, 0], [0, 0, 0]])
    ]


class TestSolutionZeroMatrix:
    __solution = SolutionZeroMatrix()

    @pytest.mark.parametrize('matrix, zero_matrix', get_testdata())
    def test_zero_matrix_algorithm(self, matrix, zero_matrix):
        self.__solution.set_input(matrix)
        self.__solution.set_zeros_bruteforce()
        assert are_identical_matrices(self.__solution.get_zeromatrix(), zero_matrix)
