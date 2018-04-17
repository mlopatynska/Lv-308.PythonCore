flag = False
while not flag:
    sum = input("Input sum of numbers (it must be integer in the interval [1, 36])...\n")
    if isinstance(sum, int) and sum >= 1 and sum <= 36:
        flag = True
for num in range(1000,10000):
    num_list = list(str(num))
    num_sum = int(num_list[0]) + int(num_list[1]) + int(num_list[2]) + int(num_list[3])
    if num_sum == sum:
        print(num)