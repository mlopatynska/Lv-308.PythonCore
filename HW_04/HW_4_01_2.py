count = 0
num = int(input('Enter a positive number: '))
while num < 1:
    num = int(input('Please, enter a positive number : '))
for i in range(1, num+1):
    if not num % i:
        count += 1
    if count > 2:
        print('It\'s not a prime number')
        break
else:
    print('It\'s a prime number')
