from math import* 

# Enter variables x, y, z

x = float(input("Enter the variable x: "))
y = float(input("Enter the variable y: "))
z = float(input("Enter the variable z: "))

# Task "a"

a = (sqrt(fabs(x - 1)) - (fabs(y))**(1/3))/(1 + x**2/2 + y**2/4)
b = x * (atan(z) + exp(-(x + 3)))
   
print("The solution of the task A:\n a = {}\n b = {}\n".format(a, b))

# Task "b"

a = (3 + exp(y - 1))/(1 + x**2 * fabs(y - tan(z)))
b = 1 + fabs(y - x) + ((y - x)**2/2) + (fabs(y - x)**3)/3

print("The solution of the task B:\n a = {}\n b = {}\n".format(a, b))

# Task "c"

a = (1 + y)* (x + y/x**2 + 4)/(exp(-x-2) + 1)/(x**2 + 4)
b = (1 + cos(y - 2))/(x**4/2 + sin(z)**2)

print("The solution of the task C:\n a = {}\n b = {}\n".format(a, b))

# Task "d"

a = y + x / y**2 + fabs(x**2 / y + x**3 / 3)
b = (1 + tan(z / 2)**2)

print("The solution of the task D:\n a = {}\n b = {}\n".format(a, b))

# Task "e"

a = (2 * cos(x - pi / 6)) / (1 / 2 + (sin(y))**2)
b = 1 + (z**2) / (3 + z**2 / 5)

print("The solution of the task E:\n a = {}\n b = {}\n".format(a, b))

# Task "f"

a = (1 + (sin(x + y))**2) / (2 + fabs(x - 2 * x /(1 + x**2 * y**2))) + x
b = (cos(atan(1 / z)))**2

print("The solution of the task F:\n a = {}\n b = {}\n".format(a, b))

# Task "g"

a = log(fabs(y - (sqrt(fabs(x)) * (x - y / z + x**2/4))))
b = x - (x**2 / factorial(3)) + (x**5 / factorial(5))

print("The solution of the task G:\n a = {}\n b = {}\n".format(a, b))