flag = False
while not flag:
    num = input("Input positive integer number...\n")
    if isinstance(num, int) and num >= 1:
        flag = True
list = []
for mul in range(1, num+1):
    if not(num % mul):
        list.append(mul)
print("{} is a prime number".format(num) if len(list) == 2
      else "{} is not a prime number because it has such dividers: {}. ".format(num, list))

