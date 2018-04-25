def mysort(mas):
    for m in range(len(mas)-1):
        for n in range(len(mas)-1):
            if mas[n]<mas[n+1]:
                mas[n], mas[n+1] = mas[n+1], mas[n]
    return mas


a = input("Input array a...\n")
b = input("Input array b...\n")
print("Sorted array 'a' is {}.".format(mysort(a)))
print("Sorted array 'b' is {}.".format(mysort(b)))