num = raw_input("I.  The number between 1000 and 9999 is...\n")
num_list = list(num)
prod = int(num_list[0])*int(num_list[1])*int(num_list[2])*int(num_list[3])

print("The product of numbers is {}. \n"
      "The number in reverse order is {}{}{}{}. \n"
      "The sorted numbers look like {}.".format(prod,
                                                num_list[3],
                                                num_list[2],
                                                num_list[1],
                                                num_list[0],
                                                sorted(num_list)))


Num = input("II.  The number between 1000 and 9999 is...\n")

Num_list = list(str(Num))
prod = (Num/1000) * (Num/100%10) * (Num/10%10) * (Num%10)
revers = (Num/1000) + 10 * (Num/100%10) +100 * (Num/10%10) + 1000 * (Num%10)

print("The product of numbers is {}. \n"
      "The number in reverse order is {}. \n"
      "The sorted numbers look like {}.".format(prod,
                                                revers,
                                                sorted(Num_list)))


