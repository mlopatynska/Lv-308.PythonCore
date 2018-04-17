flag = False
while not flag:
    num = input("Input positive integer number...\n")
    if isinstance(num, int) and num >= 1:
        flag = True
sum = 0
num_list = list(str(num))
for count in num_list:
    sum += (int(count))**3

print("The sum of the digit cubes of the number {} is equal to {}.".format(num, sum))