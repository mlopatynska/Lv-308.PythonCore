from math import*

print("Enter the coefficients for the quadratic equation (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# We find a discriminant by the formula
D = b**2 - 4 * a * c

print("Discriminant D =", D)
if D > 0:
	x1 = (-b + math.sqrt(D)) / (2 * a)
	x2 = (-b - math.sqrt(D)) / (2 * a)
	print("The equation has one roots", x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print("The equation has one root", x)
else:
    print("The equation has no roots")