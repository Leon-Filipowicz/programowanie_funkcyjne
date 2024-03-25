def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(example))
