import pytest

from ctcl.chapter1.arrays_strings.rotate_matrix import SolutionRotateMatrix


def get_testdata():
    return [
        ([[1, 2], [3, 4]],
         [[3, 1], [4, 2]]),
        ([[7, 2, 3], [5, 9, 8], [1, 0, 6]],
         [[1, 5, 7], [0, 9, 2], [6, 8, 3]]),
        ([[100]], [[100]]),
        ([[5, 0, 6, 3], [4, 15, 7, 3], [2, 0, 7, 1], [8, 9, 9, 8]],
         [[8, 2, 4, 5], [9, 0, 15, 0], [9, 7, 7, 6], [8, 1, 3, 3]])
    ]


def are_identical(output_matrix, expected_matrx):
    rows, columns = len(expected_matrx), len(expected_matrx[0])
    return all([output_matrix[row][column] == expected_matrx[row][column]
                for row in range(rows) for column in range(columns)])


class TestSolutionRotateMatrix:
    __solution = SolutionRotateMatrix()

    @pytest.mark.parametrize('matrix, rotated_matrix', get_testdata())
    def test_rotate_matrix(self, matrix, rotated_matrix):
        self.__solution.set_input(matrix)
        self.__solution.rotate_matrix()
        assert are_identical(self.__solution.get_output(), rotated_matrix)
