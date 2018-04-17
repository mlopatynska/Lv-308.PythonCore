"""password = raw_input("Enter password: ")

if len(password) >= 3 and len(password) <= 6:
    print "Welcome to the site, the lenght of your pass was {}".format(len(password))
elif len(password) < 3:
    print"The lenght of your password is too short!"
else:
    print "The lenght of your password is too long !"
print "Finish" """




goods = raw_input("How many goods do you want to bye?:")
if goods > 100:
    print "You discount is 10%"
elif goods > 50:
    print "You discount is 2%"
elif goods > 20:
    print "You discount is 1%"


