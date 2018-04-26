def fact(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


def task(m, n):
    result = fact(m) * fact(n) / fact(m + n)
    return result


print(task(2, 2))

