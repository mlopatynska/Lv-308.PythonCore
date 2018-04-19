firstNumber, nextNumber, count = 1, 1, 0
num = int(input('Enter a number : '))
print(f'First {num} Fibonacci numbers: ')
while count < num:
    print(firstNumber)
    sum = firstNumber + nextNumber
    firstNumber, nextNumber = nextNumber, sum
    count += 1


