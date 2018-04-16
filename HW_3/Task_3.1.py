"""in accordance with the Gregorian calendar,
the year is a leap year if its number is a
multiple of 4, but not a multiple of 100, and a
lso if it is a multiple of 400."""

a = int(input("Enter a number of year "))
if a % 4 == 0 and a % 100!=0:
    print("It's a leap year!")
elif a % 400 == 0:
    print("It's a leap year")
else:
    print("This is not leap year!")
