import copy, random, re
test_list = str(input("Print 3 str: "))

# making full new copy of list
new_list = copy.deepcopy(test_list)
print("First list id",id(test_list))
print(test_list)
print("Second list id",id(new_list))
print(new_list)
one, two, three = test_list[0], test_list[1], test_list[2]
print(one, two, three)
long_list = str(input("Print ∞ str "))

# getting 1/3 len of the list
partslist = int(len(long_list)/3)

listone = long_list[:partslist]

listtwo = long_list[partslist:partslist+partslist]

listthree = long_list[partslist+partslist:]

onelong, twolong, threelong = listone, listtwo, listthree

print(onelong, twolong, threelong)
rad = int(input("Write your radius: "))
print((rad-1)**2 + rad**2)
is_pandigit = str(input("Write yor digits: "))

print(len(str(1234567890)) == len(list(set(is_pandigit).intersection(set(str(1234567890))))))
shift = int(input("Write your n number: "))
circle_list = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
print(circle_list[shift])