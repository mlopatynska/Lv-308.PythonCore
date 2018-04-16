from calendar import monthrange
year = int(input("Print your year: "))
if ((year / 4).is_integer() and year / 100 != 0) or (year / 400).is_integer():
    print("It's a leap year!")
else:
    print("This is not a leap year!")


day, month, year = int(input("\nDay: ")), int(input("Month: ")),\
                   int(input("Year: "))

mthrange = monthrange(year, month)
if (day >= 1 and day in range(mthrange[0], mthrange[1])) and (month >= 1 and month <= 12) and (year >= 0):
    print("True" + "\n" + str(day) + "." + str(month) + "." + str(year))
else:
    print("Err")

a = float(input("\na: "))
b = float(input("b: "))
c = float(input("c: "))

Discriminant = b ** 2 - 4 * a * c

if Discriminant > 0:
    from math import sqrt
    x1 = (-b + sqrt(Discriminant)) / (2 * a)
    x2 = (-b - sqrt(Discriminant)) / (2 * a)
    print("1x = {}\n2x = {}".format(x1, x2))
elif Discriminant == 0:
    x = -b / (2 * a)
    print("x = ", x)
else:
    print("Err")

sidea, sideb, sidec = int(input("\nSide a: ")), int(input('Side b: ')), int(input('Side c: '))
if sidea >= 1 and sideb >= 1 and sidec >= 1:
    from math import sqrt
    P = (sidea+sideb+sidec)/2
    print("True\nP = {}\nS = {}".format(P, sqrt(P * (P-sidea) * (P-sideb) * (P-sidec))))
else:
    print("Err\n")


day_list = list(range(1, 366))
day = int(input("\nPrint day(1 - 365)"))
print(bool(day in day_list[0::7]))
if day in day_list[0::7]:
    print('Monday')
elif day in day_list[1::7]:
    print('Tuesday')
elif day in day_list[2::7]:
    print('Wednesday')
elif day in day_list[3::7]:
    print('Thursday')
elif day in day_list[4::7]:
    print('Friday')
elif day in day_list[5::7]:
    print('Saturday')
elif day in day_list[6::7]:
    print('Sunday')
else:
    print('Err')
print('\nMonday day_list: ', day_list[0::7])
print('Tuesday day_list: ', day_list[1::7])
print('Wednesday day_list: ', day_list[2::7])
print('Thursday day_list: ', day_list[3::7])
print('Friday day_list: ', day_list[4::7])
print('Saturday day_list: ', day_list[5::7])
print('Sunday day_list: ', day_list[6::7])