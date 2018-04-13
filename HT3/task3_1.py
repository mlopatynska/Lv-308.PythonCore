
year = input("Enter some year, what you want: ")

print 'It\'s a leap year' if (year % 4 and year % 100) or not year % 400 else 'It\'s not a leap year'
