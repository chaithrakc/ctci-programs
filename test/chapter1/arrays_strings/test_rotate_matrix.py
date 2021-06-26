import pytest

from ctcl.chapter1.arrays_strings.rotate_matrix import SolutionRotateMatrix


def get_testdata():
    return [
        (),
        (),
        ()
    ]


class TestSolutionRotateMatrix:
    __solution = SolutionRotateMatrix()

    @pytest.mark.parametrize('matrix, rotated_matrix', get_testdata())
    def test_rotate_matrix(self, matrix, rotated_matrix):
        self.__solution.set_input(matrix)
        self.__solution.rotate_matrix()
        assert self.__solution.get_output() == rotated_matrix
