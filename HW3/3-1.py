#Leap or not leap Year
Y = int(input('Enter Year:\n'))
if Y % 4 != 0 or Y % 100 == 0 and Y % 400 == 1:
    print('\n{} is not leap Year'.format(Y))
else:
    print(f'{Y} is leap Year')




#or this way
import calendar
x = int(input("Enter year:\n"))
if calendar.isleap(x) is True:
    print("This year is leap")
else:
    print("This year is not leap")


