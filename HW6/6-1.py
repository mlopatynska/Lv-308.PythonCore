# determine the value
def func(var_1, var_2):
    for i in range(30):
        res = (var_1 + i) * var_2 ** (30 - i)
        return res


a, b, c = 2, 7, 6
x, y, z = 1, 5, 9


result1 = func(a, x,)
result2 = func(b, y)
result3 = func(c, x + z)
print((result1**2 - result2)/result3)