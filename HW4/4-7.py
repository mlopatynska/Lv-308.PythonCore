list_a =[ ['*']*5]
for i in range(0, len(list_a)):
    row = " "
    for j in range (0, len(list_a[i])):
        row += str(list_a[i][j])
        print (row)

