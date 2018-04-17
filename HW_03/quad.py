from math import sqrt
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

if a == 0:
    print('It\'s not a quadratic equation')
else:
    d = (b**2) - (4*a*c)
    if d == 0:
        print(f'There is one solution: {-b/2*a}')
    elif d > 0:
        print(f'The solution are {(-b-sqrt(d))/(2*a):.4} and {(-b+sqrt(d))/(2*a):.4}')
    else:
        print('There\'s no solution')
