a = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, -1, -2, -3, -4, -5, -6, 0, -1, -2, -3, -4, -5, -6, 1, 1, 1.0]
b = [1, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, -1, -2, -3, -4, -5, -6, 0, -1, -2, -3, -4, -5, -6, 1, 2.0]
c = [1, 1, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, -1, -2, -3, -4, -5, -6, 0, -1, -2, -3, -4, -5, -6, -4.0]

def polinom(mas, var):
    f = 0
    for k in range(31):
        f += mas[k] * x**(30-k)
    return f

x = input("Input variable x...\n")
y = input("Input variable y...\n")
z = input("Input variable z...\n")

print("The value of function os equal to {}.".format(((polinom(a, x))**2 - polinom(b, y))/polinom(c, x+z)))

