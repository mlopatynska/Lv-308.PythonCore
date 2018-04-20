#find all four-digit numbers whis sum equal to given number
# min and max sum of it's 1-36
num = int(input("Enter any number in range 1-36:\n"))
if 1 <= num <= 36:
    for i in range(1000, 10000):
        list_num = list(str(i))
        list_sum = int(list_num[0])+ int(list_num[1]) + int(list_num[2]) + int(list_num[3])
        if list_sum == num:
           print(i)
           continue
else:
    print("Enter valid number")
