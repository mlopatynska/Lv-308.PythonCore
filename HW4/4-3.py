#Fibonacci
num = int(input("Input number:\n"))
if num >= 0:
    a, b = 0, 1
    for i in range(0, num + 1):
        a, b = b, a + b
        print(b)
else:
    print("0")