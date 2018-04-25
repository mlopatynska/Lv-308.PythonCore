
def factorial(var):
    if var == 0 or var == 1:
        return 1
    elif var < 0:
        return False
    else:
        return float(var * factorial(var-1))
# The function who finding factorial number's


var_m = input('Enter any "m" number: ')
var_n = input('Enter any "n" number: ')

print factorial(var_m)*factorial(var_n)/factorial(var_n+var_m)
