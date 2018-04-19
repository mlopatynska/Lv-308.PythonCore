
finish = False
while not finish:
    num = input('Enter a number from 1 to 36: ')

    if 0 >= num > 36:
        print 'You\'ve typed incorrect number. Please try again.'
        finish = False
    else:
        for x in range(1000, 10000):
            digit_num = list(str(x))
            num_dig = int(digit_num[0]) + int(digit_num[1]) + int(digit_num[2]) + int(digit_num[3])
            if num == num_dig:
                print 'This 4 digit number {} in summary give {}'.format(x, num)
                finish = True
                break
