def LinearSearch(mas, x):
    i = 0
    length = len(mas)-1
    while i < len(mas) and mas[i] != x:
        print(i)
        i += 1
	return i if i < len(mas) else None

List = [3,5,9,7,6,12,15,9,1]
num1 = input("What number are you looking for? ")
num2 = linearSearch(num1, List)
if num2:
    print("The number is in index: ")
else:
    print("The number is not in the list")
