num = input('Give me a four digit number: ')
print("Sum of digits is: {}\nReverse order of digits is: {}\nSorted order is: {}".format(
                                                                                         int(num[0]) * int(num[1])
                                                                                         * int(num[2]) * int(num[3]),
                                                                                         num[::-1], sorted(num))
      )

