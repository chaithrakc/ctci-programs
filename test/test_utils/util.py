def are_identical_matrices(output_matrix, expected_matrx):
    rows, columns = len(expected_matrx), len(expected_matrx[0])
    for row in range(rows):
        for column in range(columns):
            if output_matrix[row][column] != expected_matrx[row][column]:
                return False
    return True
