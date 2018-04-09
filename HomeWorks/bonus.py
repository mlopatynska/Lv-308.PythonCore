import copy, random
test_list = []
for _ in range(0, 3):
    test_list.append(str(random.randrange(100)))
new_list = copy.deepcopy(test_list)
print(id(test_list))
print(test_list)
print(id(new_list))
print(new_list)
one, two, three = test_list
long_list = []
for _ in range(0, random.randrange(4,30)):
    long_list.append(str(random.randrange(100)))
partslist = int(len(long_list)/3)
listone = long_list[:partslist]
listtwo = long_list[partslist:partslist+partslist]
listthree = long_list[partslist+partslist:]
onelong, twolong, threelong = listone,listtwo, listthree
print(onelong, twolong, threelong)
rad = int(input("Write your radius: "))
print((rad-1)**2 + rad**2)
pandigit = str(input("Write yor digits: "))
if "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" and "0" in pandigit:
    print("True")
else:
    print("False")
shift = int(input("Write your n number: "))
circle_list = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
print(circle_list[shift])