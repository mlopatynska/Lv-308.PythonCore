import math


a = int(input("Please enter a variable: "))
b = int(input("Please enter b variable: "))

sum = a + b
minus = a - b
division = a/b
multiplication = a*b

print("Sum of numbers are: " + str(sum))
print("Minus of numbers are: " + str(minus))
print("Division of numbers are: " + str(division))
print("Multiplication of numbers are: " + str(multiplication))
print("Factorial of number a is: " + str(math.factorial(a)))
print("Factorial of number b is: " + str(math.factorial(b)))

def res(first, second, op):
    if op=='+':
        print(first+second)
    if op=='-':
        print(first-second)
    if op=='/':
        print(first/second)
    if op=='*':
        print(first*second)

res(a, b, '-')