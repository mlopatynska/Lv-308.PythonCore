year = input("Input the number of the year (A.D.)...\n")

if not isinstance(year, int) or year <=0:
    print("There is no such number for the year")
elif (not year % 4 and year % 100) or (not year % 4 and not year % 400):
    print("It's a leap year!")
else:
    print("This is not a leap year!")