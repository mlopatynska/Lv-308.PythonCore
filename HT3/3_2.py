import calendar

year = input('Enter some year: ')
month = input('Enter some month: ')
day = input('Enter some day: ')


if month > 13 or month <= 0:
    print 'You\'ve typed the wrong month, please try again.'
elif day <= calendar.monthrange(year, month)[1]:
    print "Your date correct: {}/{}/{}".format(year, month, day)
else:
    print 'You\'ve typed the wrong day, please try again.'
"""
In first, we must put month in frame, if we want, that 
method 'calendar.monthrange' haven't a row with us
"""
