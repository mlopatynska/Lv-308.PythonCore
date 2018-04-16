import datetime
# Enter the date
Y = int(input("Enter year: "))
M = int(input("Enter month: "))
D = int(input("Enter day: "))

if M > 12 or D > Y:
    print("You entered incorrect data")
else:
    date = datetime.date(Y, M, D)
    print("Date is correct")
