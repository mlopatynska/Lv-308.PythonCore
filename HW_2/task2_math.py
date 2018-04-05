from math import *

x = float(raw_input("Variable x is equal to...\n"))
y = float(raw_input("Variable y is equal to...\n"))
z = float(raw_input("Variable z is equal to...\n"))


fun_a = (sqrt(fabs(x - 1)) - (fabs(y))**(1.0/3)) / (1 + x**2/2 + y**2/4)
fun_b = x * (atan(z) + exp(-(x + 3)))
print("A)  a = {}; b = {}.".format(fun_a, fun_b))

fun_a = (3 + exp(y - 1)) / (1 + x**2 * fabs(y - tan(z)))
fun_b = 1 + fabs(y - x) + (y - x)**2/2 + (fabs(y - x))**3/3
print("B)  a = {}; b = {}.".format(fun_a, fun_b))

fun_a = (1 + y)*(x + y/(x**2 + 4)) / (exp(-x - 2) + 1/(x**2 + 4))
fun_b = (1 + cos(y - 2))/(x**4/2 + (sin(z))**2)
print("C)  a = {}; b = {}.".format(fun_a, fun_b))

fun_a = y + x / (y**2 + fabs(x**2/(y + x**3/3)))
fun_b = 1 + (tan(z/2)**2)
print("D)  a = {}; b = {}.".format(fun_a, fun_b))

fun_a = (2 * cos(x - pi/6)) / (1.0/2 + (sin(y))**2)
fun_b = 1 + z**2/(3 + z**2/5)
print("E)  a = {}; b = {}.".format(fun_a, fun_b))

fun_a = (1 + (sin(x + y))**2) / (2 + fabs(x - 2*x/(1 + x**2 * y**2))) + x
fun_b = (cos(atan(1/z)))**2
print("F)  a = {}; b = {}.".format(fun_a, fun_b))

fun_a = log(fabs((y - sqrt(fabs(x))) * (x - y/(z + x**2/4))))
fun_b = x - x**2/factorial(3) + x**5/factorial(5)
print("G)  a = {}; b = {}.".format(fun_a, fun_b))