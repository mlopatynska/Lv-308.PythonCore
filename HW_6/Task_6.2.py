def factorial(d):
     if d == 0:
          return 1
     else:
         return factorial(d-1) * d

n = int(input("Input number n "))
m = int(input("Input number m "))

print(factorial(n) * factorial(m)/factorial(n+m))