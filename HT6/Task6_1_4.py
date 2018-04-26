
matrix1 = [
                [0, 0, 1, 2, 0],
                [2, 1, 0, 0, 0],
                [1, 0, 2, 3, 2],
                [0, 0, 2, 0, 1],
                [0, 0, 5, 1, 2]
]

matrix2 = [
                [0, 1, 0, 3, 0],
                [2, 1, 0, 2, 0],
                [1, 1, 1, 0, 0],
                [0, 2, 2, 2, 1],
                [0, 4, 0, 0, 1]
]


def find_in_matrix(mat):
    max_number = 0
    max_row = 0
    max_column = 0

    for column, rows in enumerate(mat):
        for row, num in enumerate(rows):
            if num > max_number or max_number == 0:
                max_number = num
                max_column = column
                max_row = row

    return max_column, max_row, max_number
# Define where placing max number in the matrix


mat1 = find_in_matrix(matrix1)
mat2 = find_in_matrix(matrix2)
# Short for better reading

matrix1[mat1[0]][mat1[1]] = mat2[2]
matrix2[mat2[0]][mat2[1]] = mat1[2]
# Changing our max number in matrix's


