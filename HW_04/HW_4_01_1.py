num = int(input('Enter a number in range 1 - 36 : '))
while num > 36 or num < 1:
    num = int(input('Please, enter number in range 1 - 36: '))
for sum in range(1000, 10000):
    actualNum = sum
    sum = str(sum)
    sum = int(sum[0]) + int(sum[1]) + int(sum[2]) + int(sum[3])
    if sum == num:
        print(f'{num} is the sum of numbers of {actualNum}')


