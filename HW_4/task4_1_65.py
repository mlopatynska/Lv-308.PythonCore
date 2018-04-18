from math import fabs
flag = False
while not flag:
    a, b, step, pohybka = float(input("Input your a from (-1, 1)...\n")), \
                          float(input("Input your b from (-1, 1) and b>a...\n")), \
                          float(input("Input your step 0<h<b-a...\n")), \
                          float(input("Input your error (it must be between 0 and 1)...\n"))
    if a > -1 and a < 1 and b > -1 and b < 1 and b > a and step > 0 and step < b-a and pohybka < 1 and pohybka > 0:
        flag = True
x = a
while x <= b:
    y = (1+x) / (1-x)**2
    sum = 1
    k = 0
    p = 1
    while p > pohybka:
        k += 1
        sum += (2*k+1)*x**k
        if y != 0:
            p = fabs((sum - y)/y)*100
        else:
            p = 0
            break
    print("x = {:.3f}, S = {:.6f}, y = {:.6f}, p = {:.6f}".format(x, sum, y, p))
    x += step
