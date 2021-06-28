'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Hints: #51, # 100

Difficulty : Hard

'''
from typing import List


class SolutionRotateMatrix:
    matrix = None
    length = 0

    def set_input(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix
        self.length = len(matrix)

    def rotate_matrix_clockwise(self) -> None:
        if self.length != len(self.matrix[0]):  # accepting only N x N matrices for rotation
            return
        for layer in range(int(self.length / 2)):
            first = layer
            last = self.length - layer - 1
            for i in range(first, last):
                offset = i - first
                top = self.matrix[first][i]  # save top
                # left -> top
                self.matrix[first][i] = self.matrix[last - offset][first]
                # bottom -> left
                self.matrix[last - offset][first] = self.matrix[last][last - offset]
                # right -> bottom
                self.matrix[last][last - offset] = self.matrix[i][last]
                # top -> right
                self.matrix[i][last] = top  # right < - saved top

    def get_output(self) -> List[List[int]]:
        return self.matrix
