def Binary_Search(mas, x):
    i = 0
    j = len(mas)-1
    m = int(j/2)
    while mas[m] != x and i < j:
        if x > mas[m]:
            i = m + 1
        else:
            j = m - 1
        m = int((i+j)/2)
    if i > j:
        return ("Invalid data")
    else:
        return m