"""implement Home Work 02"""

import math

A = int(input("Please enter a variable: "))
B = int(input("Please enter b variable: "))

SUM = A + B
MINUS = A - B
DIVISION = A / B

MULTIPLICATION = A * B

print("Sum of numbers are: " + str(SUM))
print("Minus of numbers are: " + str(MINUS))
print("Division of numbers are: " + str(DIVISION))
print("Multiplication of numbers are: " + str(MULTIPLICATION))
print("Factorial of number a is: " + str(math.factorial(A)))
print("Factorial of number b is: " + str(math.factorial(B)))


def res(first, second, operator):
    """
    Print result of two variables.
    :param first: int
    :param second: int
    :param operator: str ['+', '-', '/', '*']
    :return: None
    """
    if operator == '+':
        print(first + second)
    if operator == '-':
        print(first - second)
    if operator == '/':
        print(first / second)
    if operator == '*':
        print(first * second)


res(A, B, '-')
