"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
Hints:#17, #74, #702

Difficulty : Easy
"""
from typing import List


class SolutionZeroMatrix:
    __zero_matrix = None
    __rows = None
    __columns = None

    def set_input(self, matrix: List[List[int]]) -> None:
        self.__zero_matrix = matrix

    def set_zeros_bruteforce(self) -> None:
        self.__rows = len(self.__zero_matrix)
        self.__columns = len(self.__zero_matrix[0])
        zero_rows = set()
        zero_columns = set()
        for row in range(self.__rows):
            for column in range(self.__columns):
                if self.__zero_matrix[row][column] == 0:
                    zero_rows.add(row)
                    zero_columns.add(column)
        self.nullify_rows(zero_rows)
        self.nullify_columns(zero_columns)

    def nullify_rows(self, zero_rows):
        for row in zero_rows:
            for column in range(self.__columns):
                self.__zero_matrix[row][column] = 0

    def nullify_columns(self, zero_columns):
        for row in range(self.__rows):
            for column in zero_columns:
                self.__zero_matrix[row][column] = 0

    def get_zeromatrix(self) -> List[List[int]]:
        return self.__zero_matrix
