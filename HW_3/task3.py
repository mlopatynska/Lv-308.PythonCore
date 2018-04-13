from math import sqrt
a = float(input("Input coefficient 'a' of the quadratic equation ax^2+bx+c=0...\n"))
b = float(input("Input coefficient 'b' of the quadratic equation ax^2+bx+c=0...\n"))
c = float(input("Input coefficient 'c' of the quadratic equation ax^2+bx+c=0...\n"))
if a==0:
    print("Your equation {}x^2+{}x+{}=0 is not quadratic.".format(a, b, c))
    if b!=0:
        print("But solution of this equation  is x = {:.4f}.".format(- c/b ))
    elif c==0:
        print("But all real x are solutions of this equation.")
    else:
        print("And there is not solution of this equation.")
else:
    d = b**2 - 4*a*c
    if d > 0:
        print("There are two real solutions of this equation: "
              "x1 = {:.4f}, x2 = {:.4f}.".format((- b + sqrt(d))/(2*a), (- b - sqrt(d))/(2*a)))
    elif d==0:
        print("This equation has one real solution (or two equal roots): "
              "x1 = x2 = {:.4f}.".format(- b/(2 * a)))
    else:
        print("There are two complex solutions of this equation: "
              "x1 = {0:.3f} + {1:.3f}j, x2 = {0:.3f} - {1:.3f}j.".format(- b/(2*a),(sqrt(-d))/(2 * a)))

