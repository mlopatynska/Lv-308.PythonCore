
a = [[1, 2, 3, 45, 678], [11, 12, 13, 14, 1567], [3, 5, 245, 2345, -12], [123, 45, 6542, 22, 567], [5, 6, 7, 8, 9]]
b = [[123, 34, 3, 4, 2], [1, 0, -1, 3, 5], [43, 3, 345, 11, 6], [1, 1, 1, 1, 1], [12345, 45, 87, 6, 89]]


def max_list_ad(my_list):
    the_biggest = my_list[0][0]
    row, col = 0, 0
    for i in range(5):
        for j in range(5):
            if the_biggest < my_list[i][j]:
                the_biggest = my_list[i][j]
                row, col = i, j
    return row, col  #the_biggest, row, col


row_a, col_a = max_list_ad(a)
row_b, col_b = max_list_ad(b)
a[row_a][col_a], b[row_b][col_b] = b[row_b][col_b], a[row_a][col_a]
print(a)
print(b)
