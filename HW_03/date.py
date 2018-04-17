import datetime
year, month, day = int(input("Enter year: ")), int(input("Enter month: ")), int(input("Enter day: "))
if datetime.date(year, month, day):
    print("Your date is correct")



