from math import fabs, sqrt
a = float(input("Input length of the first side of the triangle...\n"))
b = float(input("Input length of the second side of the triangle...\n"))
c = float(input("Input length of the third side of the triangle...\n"))
if a<=0 or b<=0 or c<=0:
    print("Your data are incorrect")
elif a+b > c and fabs(a-b) < c:
    p = (a + b + c)/2
    print("You can build a triangle with the sides a={}, b={}, c={}. "
          "Its perimeter is {}. Its area is {:.3f}. ".format(a, b, c, a+b+c, sqrt(p*(p-a)*(p-b)*(p-c))))
else:
    print("You can't build a triangle with the sides a={}, b={}, c={}.".format(a, b, c))