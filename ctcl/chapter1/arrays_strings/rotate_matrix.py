# Difficulty : Medium
from typing import List


class SolutionRotateImage:
    __matrix = None

    def set_input(self, matrix: List[List[int]]) -> None:
        self.__matrix = matrix

    def rotate_matrix_clockwise(self) -> None:
        # accepting only N x N matrices for rotation
        if len(self.__matrix) != len(self.__matrix[0]):
            return

    def get_output(self) -> List[List[int]]:
        return self.__matrix
