fibo_numb = input('Enter any number: ')
list_fibo = [fibo_numb, fibo_numb]
# The fibonacci numbers, are start from two indetic

for x in range(0, 8):
    list_fibo.append(list_fibo[x] + list_fibo[-1])
print list_fibo
