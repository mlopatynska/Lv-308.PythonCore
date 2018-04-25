def coor_max(mas):
    ar_max = mas[0][0]
    coor_i = 0
    coor_j = 0
    for i in range(5):
        for j in range(5):
            if mas[i][j] > ar_max:
                ar_max = mas[i][j]
                coor_i = i
                coor_j = j
    return(coor_i,coor_j)

a=[[1,1,1,1,1],[1,2,3,3,3],[1,1,1,1,1],[1,2,3,3,3],[1,1,9,1,1]]
b=[[1,1,1,1,1],[1,2,3,3,3],[6,15,1,1,1],[1,2,3,3,3],[1,1,-2,1,1]]

print(coor_max(a))
print(coor_max(b))

b[coor_max(b)[0]][coor_max(b)[1]], a[coor_max(a)[0]][coor_max(a)[1]] = \
    a[coor_max(a)[0]][coor_max(a)[1]], b[coor_max(b)[0]][coor_max(b)[1]]
print("The changed array 'a' has the form {}.".format(a))
print("The changed array 'b' has the form {}.".format(b))