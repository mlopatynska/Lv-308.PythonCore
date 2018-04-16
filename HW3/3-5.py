'''Name of weekday by day number.
Year is not leap & first day of year is Monday'''

day_n = int(input('Enter day of year in range 1-365: '))
week = [ 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday',  'Sunday' ]
if day_n > 365 or day_n <= 0:
    print(' Invalid date! ')
elif(day_n % 7 )== 0:
    print(f' This day of year is {week[0]}')
elif (day_n % 7 )== 1:
    print(f' This day of year is {week[1]}')
elif (day_n % 7 )== 2:
    print(f' This day of year is {week[2]}')
elif (day_n % 7 )== 3:
    print(f' This day of year is {week[3]}')
elif (day_n % 7 )== 4:
    print(f' This day of year is {week[4]}')
elif (day_n % 7 )== 5:
    print(f' This day of year is {week[5]}')  
elif (day_n % 7 )== 6:
    print(f' This day of year is {week[6]}')
