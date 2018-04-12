# Enter the four-number value
n = int(input("Enter a natural number:" ))

d1 = n // 1000
d2 = n // 100 % 10
d3 = n // 10 % 10
d4 = n % 10

print("The product of numbers of a natural value:", d1*d2*d3*d4)
# Enter the four-number value as list
n = list(input())
print("Reverse 'n' is:", n[::-1])
