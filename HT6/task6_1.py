def vars(var1, var2, var3, x, y, z):
    sqr = 30
    sum_var1 = 0
    sum_var2 = 0
    sum_var3 = 0

    for real in range(var1, var1+30):
        sum_var1 += real * x**sqr
        sqr -= 1
    sum_var1 += max(range(var1, var1+30))

    for real in range(var2, var2+30):
        sum_var2 += real * y**sqr
        sqr -=1
        sum_var2 += max(range(var2, var2 + 30))

    for real in range(var3, var3 + 30):
        sum_var3 += real * (x + z)**sqr
        sqr -=1
        sum_var3 += max(range(var3, var3 + 30))

    return (sum_var1 - sum_var2) / sum_var3

vars(0, 0, 0, 5, 2, 3)




