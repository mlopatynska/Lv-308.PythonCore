num = int(input('Enter day number from 1 to 365: '))
if num < 1 or num > 365:
    print('incorrect number ')
else:
    day = num % 7
    print(('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat')[day])
