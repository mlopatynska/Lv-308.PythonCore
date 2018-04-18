from math import fabs, exp, factorial
flag = False
while not flag:
    a, b, step, pohybka = float(input("Input any real a...\n")), \
                          float(input("Input b > a...\n")), \
                          float(input("Input your step 0<h<b-a...\n")), \
                          float(input("Input your error (it must be between 0 and 1)...\n"))
    if b > a and step > 0 and step < b-a and pohybka < 1 and pohybka > 0:
        flag = True
x = a
while x <= b:
    y = (x-1)*exp(x) + 1
    term = x**2/2
    sum = x**2/2
    k = 0
    p = 2
    while p > pohybka:
        k += 1
        term *= x*(k+1) / (k*(k+2))
        sum += term
        if y != 0:
            p = fabs((sum - y)/y)*100
        else:
            p = 0
            break
    print("x = {:.3f}, S = {:.6f}, y = {:.6f}, p = {:.6f}".format(x, sum, y, p))
    x += step
