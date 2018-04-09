from math import *
x = input("Enter value x: ")
y = input("Enter value y: ")
z = input("Enter value z: ")

# TASK A
a = (sqrt(fabs(x-1))-(fabs(y)**1/3))/(1+x**2/2+y**2/4)
b = x*(atan(z)+exp(-(x+3)))
print "A)\n a = {}\n b = {}".format(a, b)

# TASK B
a = (3+exp(y-1))/(1+x**2*(fabs(y-tan(z))))
b = 1+fabs(y-x)+((y-x)**2)/2
print "B)\n a = {}\n b = {}".format(a, b)

# TASK C
a = (1+y)*((x+y/(x**2+4))/exp(-x-2)+1/(x**2+4))
b = (1+cos(y-2))/(x**4/2+(sin(z))**2)
print "C)\n a = {}\n b = {}".format(a, b)

#TASK D
a = y+(x/(y**2+fabs(x**2/(y+x**3/3))))
b = (1+(tan(z/2)**2))
print "D)\n a = {}\n b = {}".format(a, b)

#TASK E
a = (2*cos(x-pi/6))/(1/2+(sin(y))**2)
b = (cos(atan(1/z)))
print "E)\n a = {}\n b = {}".format(a, b)

#TASK F
#a = x+((1+(sin(x+y))**2)/(2+fabs(x-2x/(1+x**2*y**2))))
#print "F)\n a = {} ".format(a)