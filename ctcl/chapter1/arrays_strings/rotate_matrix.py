from typing import List

'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Hints: #51, # 100

Difficulty : Medium

'''


class SolutionRotateMatrix:
    __matrix = None

    def set_input(self, matrix: List[List[int]]) -> None:
        self.__matrix = matrix

    def rotate_matrix_clockwise(self) -> None:
        # accepting only N x N matrices for rotation
        if len(self.__matrix) != len(self.__matrix[0]):
            return

    def get_output(self) -> List[List[int]]:
        return self.__matrix
