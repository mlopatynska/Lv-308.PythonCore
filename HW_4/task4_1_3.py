flag = False
while not flag:
    num = input("Input positive integer number...\n")
    if isinstance(num, int) and num >= 1:
        flag = True
list = [1]
if num >= 2:
    list.append(1)
for count in range(2, num):
    list.append(list[count-1]+list[count-2])

print("{} Fibonacci numbers are {}.".format(num, list))