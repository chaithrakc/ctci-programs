from typing import List

'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
Hints:#17, #74, #702

https://leetcode.com/problems/set-matrix-zeroes/

Difficulty : Medium
'''


class SolutionZeroMatrix:
    __matrix = None
    __rows = 0
    __columns = 0

    def set_input(self, matrix: List[List[int]]) -> None:
        self.__matrix = matrix

    # additional memory approach
    def set_zeroes(self) -> None:
        self.__rows, self.__columns = len(self.__matrix), len(self.__matrix[0])
        zero_rows, zero_columns = set(), set()
        for row in range(self.__rows):
            for column in range(self.__columns):
                if self.__matrix[row][column] == 0:
                    zero_rows.add(row)
                    zero_columns.add(column)
        for zero_row in zero_rows:
            self.__nullify_rows(zero_row)
        for zero_column in zero_columns:
            self.__nullify_columns(zero_column)

    def __nullify_rows(self, zero_row) -> None:
        for column in range(self.__columns):
            self.__matrix[zero_row][column] = 0

    def __nullify_columns(self, zero_column) -> None:
        for row in range(self.__rows):
            self.__matrix[row][zero_column] = 0

    # space efficient solution
    def set_zeroes_efficient(self) -> None:
        self.__rows, self.__columns = len(self.__matrix), len(self.__matrix[0])

        # check first row and first column has zero
        first_row_has_zero, first_col_has_zero = self.__check_first_row_column_zeroes()

        # check rest of the matrix has zero
        for row in range(1, self.__rows):
            for column in range(1, self.__columns):
                if self.__matrix[row][column] == 0:
                    self.__matrix[row][0] = 0
                    self.__matrix[0][column] = 0
        # nullify
        self.__nullify_matrix()
        if first_row_has_zero:
            self.__nullify_rows(0)
        if first_col_has_zero:
            self.__nullify_columns(0)

    def __nullify_matrix(self) -> None:
        for row in range(1, self.__rows):
            if self.__matrix[row][0] == 0:
                self.__nullify_rows(row)
        for column in range(1, self.__columns):
            if self.__matrix[0][column] == 0:
                self.__nullify_columns(column)

    def __check_first_row_column_zeroes(self, first_row_has_zero=False, first_col_has_zero=False) -> tuple:
        for column in range(self.__columns):
            if self.__matrix[0][column] == 0:
                first_row_has_zero = True
                break
        for row in range(self.__rows):
            if self.__matrix[row][0] == 0:
                first_col_has_zero = True
                break
        return first_row_has_zero, first_col_has_zero

    def get_zeromatrix(self) -> List[List[int]]:
        return self.__matrix
