#block diagram

a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))
sum = int(input("Enter sum:\n"))
x = a

while x <= b:
    y = 2*x/(1-x)**3
    s = 0
    k = 0
    p = 1
    while p > sum :
        k +=1
        S = s + k*(k + 1)* x**k
        p=(a*b*s*(s-y))/y*100
    else:
        print("{}{}{}{}".format(x, s, y, p))
        x = x + k
        break
else:
    print ("End")
