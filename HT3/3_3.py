import math

a = input("Enter 'a' number (notice 'a' can't be equal '0')")
b = input("Enter 'b' number: ")
c = input('Enter "c" number: ')

d = b**2 - 4*a*c

if a == 0:
    print 'I\'ve told you, about 0 in "a" number. please try again'
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print """
    The D > 0, that mean, this quadratic equation have a two true roots:
    x1 = (-b + sqrt(d))//(2 * a) = {}
    x2 = (-b + sqrt(d))//(2 * a) = {}
    """.format(x1, x2)
elif d == 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print """
    The D = 0, that mean, this quadratic equation have a one true root:
    x1 = (-b + sqrt(d))/(2 * a) = {}
    """.format(x1)
else:
    print "The D < 0, that mean, this quadratic equation haven't no one roots"
