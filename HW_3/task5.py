day = input("Input  number of the day 1...365\n")

if isinstance(day, int) and day > 0 and day <= 365:
    if (day % 7) == 0:
        n = "Sunday"
    elif (day % 7) == 1:
        n = "Monday"
    elif (day % 7) == 2:
        n = "Tuesday"
    elif (day % 7) == 3:
        n = "Wednesday"
    elif (day % 7) == 4:
        n = "Thursday"
    elif (day % 7) == 5:
        n = "Friday"
    else:
        n = "Saturday"
else:
    n = "Your date is incorrect"
print(n)

