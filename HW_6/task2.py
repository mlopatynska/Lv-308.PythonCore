def calc_factorial(x):
    if x == 0:
        return 1.0
    else:
        return (x * calc_factorial(x-1))

flag = False
while not flag:
    n = input("Input nonegative integer number n...\n")
    if type(n) == int and n >= 0:
        flag = True
flag = False
while not flag:
    m = input("Input nonegative integer number m...\n")
    if type(m) == int and m >= 0:
        flag = True

print("The value of function is equal to {}.".format(calc_factorial(n)*calc_factorial(m)/calc_factorial(n+m)))