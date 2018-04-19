num, result = int(input('Enter a positive number: ')), 0
while num < 1:
    num = int(input('Please, enter a positive number: '))
numProcessed = str(num)
for i in range(len(numProcessed)):
    result += int(numProcessed[i]) ** 3
print(f'The sum of the digits cubes of {num} - {result}')
