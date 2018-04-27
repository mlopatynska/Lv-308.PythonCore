# Enter matrix a and b

a = [[1,5,8,4,2],[45,5,78,1,1],[5,26,3,5,4],[1,1,1,1,1],[2,5,2,2,3]]
b = [[1,1,1,1,1],[2,2,2,1,2],[5,4,5,4,2],[1,1,1,1,1],[1,2,3,4,5]]

def max_el(matrix):
    max_el = matrix[0][0]
    max_n = 0
    max_m = 0
    for n in range(5):
        for m in range(5):
            if matrix[n][m] < max_el:
                max_el = matrix[n][m]
                max_n = n
                max_m = m
    return(max_n,max_m)

print(max_el(a))
print(max_el(b))