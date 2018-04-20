fibo_numb = input('Enter any number: ')
list_fibo = [1, 1]
# The fibonacci numbers, are start from two indetic

if fibo_numb == 1:
    print list_fibo[0]
elif fibo_numb ==2:
    print list_fibo
elif fibo_numb > 2:
    for x in range(0, fibo_numb - 2):
        list_fibo.append(list_fibo[x] + list_fibo[-1])
    print list_fibo

