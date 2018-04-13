from datetime import datetime

year = input("Input number of the year (A.D.)...\n")
month = input("Input number of the month...\n")
day = input("Input  number of the day...\n")

if not isinstance(year, int) or year <= 0 or year >= 9999:
    print("The number for the year is incorrect")
elif not isinstance(month, int) or month <= 0 or month >= 13:
    print("Month must be in 1..12")
else:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month != 2:
        max_day = 30
    elif (not year % 4 and year % 100) or (not year % 4 and not year % 400):
        max_day = 29
    else:
        max_day = 28
    if not isinstance(day, int) or day <= 0 or day > max_day:
        print("What a strange day?!")
    else:
        Your_date = datetime(year, month, day)
        My_date = datetime.now()
        print("{} is correct date! But now {}.".format(Your_date, My_date))

