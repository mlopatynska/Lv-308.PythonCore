#check if datetime is valid
from calendar import monthrange
import datetime


year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if month > 12 or day > monthrange(year, month)[1]:
    print('\n'f'{year}-{month}-{day} is incorrect date')
else:
    date = datetime.date(year, month, day)
    print(f'{date} is correct date!')











