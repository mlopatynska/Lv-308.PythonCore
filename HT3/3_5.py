
day_t = input('Enter any day from 1 to 365: ')
days = list(range(1, 366))

if day_t in days[0::7]:
    print 'Today is Monday.'
elif day_t in days[1::7]:
    print 'Today is Tuesday'
elif day_t in days[2::7]:
    print 'Today is Wednesday'
elif day_t in days[3::7]:
    print 'Today is Thursday'
elif day_t in days[4::7]:
    print 'Today is Friday'
elif day_t in days[5::7]:
    print 'Today is Saturday'
elif day_t in days[6::7]:
    print 'Today is Sunday'
else:
    print 'You typed incorrect date.'

