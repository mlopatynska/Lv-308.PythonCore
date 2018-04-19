height = int(input('Enter the height of a pyramid :)  '))
while height < 1:
    height = int(input('bigger than zero, please: '))
print('\nHalf triangle... \n')
for count in range(1, height + 1):
    print('*'*count)
print('\nFull triangle... \n')
for count in range(1, height + 1):
    print(' '*(height-count) + ('*'*(2*count-1)) + ' '*(height-count))
print('\nInverted triangle... \n')
for count in range(height, 0, -1):
    print(' '*(height-count) + ('*'*(2*count-1)) + ' '*(height-count))
