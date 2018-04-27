def fact_nat(var_f):
    """Find factorial of natural number"""
    if var_f == 0:
        return 1
    return fact_nat(var_f-1)*var_f


n = int(input("Enter number:\n"))
m = int(input("Enter number:\n"))
F = fact_nat(m)*fact_nat(n)/(fact_nat(n+m))
print(f'The result of the expression is {F}')
