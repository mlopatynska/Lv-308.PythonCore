import math

x = input("Enter x: ")
y = input("Enter y: ")
z = input("Enter z: ")

var_a = 2 * math.cos(x - (math.pi/6))/(1/2 + math.sin(y)**2)
print 'solution of the equation: a= 2cos(x-pi/6)/(1/2+sin^2y)=', var_a

var_b = 1 + (z**2)/(3 + z**2/5)
print 'solution of the equation: b= 1+(z^2/(3+z^2/5))=', var_b