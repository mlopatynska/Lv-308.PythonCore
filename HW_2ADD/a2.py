n = input(" 'Radius' of the romb is...\n")
print("This figure consists of {} squares.\n".format(n**2 + (n-1)**2))

N = input("How many points are on the circle? \n"
          "(Input even number otherwise you will get the wrong answer)\n")
firstNumber = input("What's number of the first point? "
                    "(Input number less than previous otherwise you will get the wrong answer)\n")

half = N/2
secondNumber = (1 - firstNumber/half) * half + firstNumber % half
print("The other point is {}".format(secondNumber))