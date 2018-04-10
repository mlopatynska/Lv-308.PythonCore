"""Import mathematical function
from module math"""
from math import fabs
from math import exp
from math import atan
from math import tan
from math import sin
from math import cos
from math import factorial
from math import sqrt
from math import pi
from math import log

#Assign values to variables
x = input("Enter value x: ")
y = input("Enter value y: ")
z = input("Enter value z: ")

#Solutions:

# TASK A
a = (sqrt(fabs(x-1))-(fabs(y)**1/3))/(1+x**2/2+y**2/4)
b = x*(atan(z)+exp(-(x+3)))
print "\n A)\n a = {}\n b = {}\n".format(a, b)

# TASK B
a = (3+exp(y-1))/(1+x**2*(fabs(y-tan(z))))
b = 1+fabs(y-x)+((y-x)**2)/2
print "B)\n a = {}\n b = {}\n".format(a, b)

# TASK C
a = (1+y)*((x+y/(x**2+4))/exp(-x-2)+1/(x**2+4))
b = (1+cos(y-2))/(x**4/2+(sin(z))**2)
print "C)\n a = {}\n b = {}\n".format(a, b)

#TASK D
a = y+(x/(y**2+fabs(x**2/(y+x**3/3))))
b = (1+(tan(z/2)**2))
print "D)\n a = {}\n b = {}\n".format(a, b)

#TASK E
a = (2*cos(x-pi/6))/(1/2+(sin(y))**2)
b = 1+(z**2/(3+z**2/5))
print "E)\n a = {}\n b = {}\n".format(a, b)

#TASK F
a = x+((1+(sin(x+y))**2)/(2+fabs(x-2*x/(1+x**2*y**2))))
b = (cos(atan(1/z))**2)
print "F)\n a = {} \n b = {}\n".format(a, b)

#TASK G
a = log(fabs((y - sqrt(fabs(x)))*(x-(y/(z+x**2/4)))))
b = x-(x**2/factorial(3)+x**5/factorial(5))
print "G)\n a = {} \n b = {} ".format(a, b)
