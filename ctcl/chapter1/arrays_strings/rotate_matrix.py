# Difficulty : Medium
class SolutionRotateMatrix:
    __image_matrix = None

    def set_input(self, image_matrix: list[list[int]]) -> None:
        self.__image_matrix = image_matrix

    def rotate_matrix(self) -> None:
        # accepting only N x N matrices for rotation
        if len(self.__image_matrix) != len(self.__image_matrix[0]):
            return

    def get_output(self) -> list[list[int]]:
        return self.__image_matrix
