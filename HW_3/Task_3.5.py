# From module datetime
# importing the date object

from datetime import date

D = int(input("Enter number of the day of year "))
    
if (D % 7) == 0:
    print("It Monday.")
elif (D % 7) == 1:
    print("It Tuesday.")
elif (D % 7) == 2:
    print("It Wednesday.")
elif (D % 7) == 3:
    print("It Thursday.")
elif (D % 7) == 4:
     print("It Friday.")
elif (D % 7) == 5:
    print("It Saturday.")
elif (D % 7) == 6:
    print("It Sunday.")
else:
    print("Incorrect date.")