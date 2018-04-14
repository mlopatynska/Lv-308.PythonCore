#not completed
#check if datetime is valid

from calendar import monthrange
from datetime import date
Y = int(input("Enter year:\n"))
M = int(input("Enter month:\n"))
D = input("Enter day: \n")
if M in monthrange(year, month) is True:
       print("{}-{}-{} is correct".format(Y, M, D))
else:
    print("{}-{}-{} is incorrect format of date".format(Y, M, D))
print('End') """
