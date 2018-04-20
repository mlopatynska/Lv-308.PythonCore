#Check if number is simple
import math

num = int(input("Enter number:\n"))
if num < 2:
    print("enter number >= 2")
elif num == 2:
    print("{} is  simple".format(num))
i = 2
max = int(math.sqrt(num))
while i <= max:
    if num % i == 0:
        print("{} is not simple".format(num))
        quit()
    i += 1
print("{} is simple".format(num))