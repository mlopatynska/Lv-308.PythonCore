num = int(raw_input("The number between 1000 and 9999 is...\n"))

prod = 1
revers = 0
list = []

for x in range(0, 4):
    rest = num % 10
    list.append(rest)
    prod *= rest
    revers *= 10
    revers += rest
    num = (num - rest)/10

print("The product of numbers is {}.".format(prod))
print("The number in reverse order is {}.".format(revers))
print("The sorted numbers look like {}.".format(sorted(list)))