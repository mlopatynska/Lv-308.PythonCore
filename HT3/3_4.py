import math

a = input('Enter first length: ')
b = input('Enter second length: ')
c = input('Enter third length: ')

if a >= b + c or b >= a + c or c >= a + b:
    print 'Those length can\'t create a triangle. Please try again.'
else:
    p = (a + b + c)/2
    s_geron = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print "The perimeter of triangle is {}, " \
          "and his square is {:2f}".format(p, s_geron)
