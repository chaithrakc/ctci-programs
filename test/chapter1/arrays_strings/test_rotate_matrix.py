from ctci.chapter1.arrays_strings.rotate_matrix import SolutionRotateMatrix
import pytest

from test.test_utils.util import are_identical_matrices


def get_testdata():
    return [
        ([[1, 2], [3, 4]],
         [[3, 1], [4, 2]]),
        ([[7, 2, 3], [5, 9, 8], [1, 0, 6]],
         [[1, 5, 7], [0, 9, 2], [6, 8, 3]]),
        ([[100]], [[100]]),
        ([[]], [[]]),
        ([[5, 0, 6, 3], [4, 15, 7, 3], [2, 0, 7, 1], [8, 9, 9, 8]],
         [[8, 2, 4, 5], [9, 0, 15, 0], [9, 7, 7, 6], [8, 1, 3, 3]]),
        ([[5, 0, 6, 3, 9], [4, 15, 7, 3, 0], [2, 0, 7, 1, 15], [8, 9, 9, 8, 23], [9, 7, 21, 23, 0]],
         [[9, 8, 2, 4, 5], [7, 9, 0, 15, 0], [21, 9, 7, 7, 6], [23, 8, 1, 3, 3], [0, 23, 15, 0, 9]])
    ]


class TestSolutionRotateMatrix:
    __solution = SolutionRotateMatrix()

    @pytest.mark.parametrize('matrix, rotated_matrix', get_testdata())
    def test_rotate_matrix_clockwise(self, matrix, rotated_matrix):
        self.__solution.set_input(matrix)
        self.__solution.rotate_matrix_clockwise()
        assert are_identical_matrices(self.__solution.get_output(), rotated_matrix)
