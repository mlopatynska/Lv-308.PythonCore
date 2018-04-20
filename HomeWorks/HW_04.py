#4.1
num = int(input('4.1/Enter your number: '))
num_list = []
for i in range(1000, 10000):
    i = str(i)
    range_sum = int(i[0]) + int(i[1]) + int(i[2]) + int(i[3])
    if num == range_sum:
        num_list.append(i)
if num_list:
    print(num_list)
    print("{} possible numbers".format(len(num_list)))
else:
    print("There are no such numbers")

#4.2
is_simple_number = int(input("4.2/Enter your simple(or not) number: "))
list_of_simple = [2]
for i in range(3, is_simple_number + 1, 2):
    if i > 10 and i % 10 is 5:
        continue
    for x in list_of_simple:
        if x * x - 1 > i:
            list_of_simple.append(i)
            break
        if i % x == 0:
            break
    else:
        list_of_simple.append(i)
print(bool(is_simple_number in list_of_simple))

#4.4
num = str(input("4.4/Enter your number"))
list_for_cubes = ""
for i in num:
    list_for_cubes += (str(int(i)**3)) + "+"
print(eval(list_for_cubes[:-1]))

#4.5
text = input("4.5/Text: ")
searched_symb = input("Searched symbols: ")
A = text.split(" ")
print(A)
for i in A:
    if searched_symb in i:
        print(i.replace(".", " ").replace(",", " "))