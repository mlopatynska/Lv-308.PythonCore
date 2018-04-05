import math

x = input("Enter first number: ")
y = input("Enter second number: ")
z = input("And the last one: ")

var_a = (3 + math.expm1(y))/(1 + x**2 * math.fabs(y - math.tan(z)))
print 'solution of the equation: a= (3+e^y-1)/(1+x^2|y-tg(z)| =', var_a

var_b = 1 + math.fabs(y-x) + ((y-x)**2/2) + (math.fabs(y-x)**3/3)
print 'solution of the equation: b= 1+|y-x|+((y-x)^2/2)+(|y-x|^3/3) =', var_b