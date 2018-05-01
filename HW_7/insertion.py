def insertion(mas):
    for m in range(1, len(mas)):
        if mas[m] < mas[m-1]:
            el = mas.pop(m)
            if el < mas[0]:
                mas.insert(0, el)
            else:
                for n in range(m-1,-1,-1):
                    if el >= mas[n] and el < mas[n + 1]:
                        mas.insert(n + 1, el)
    return mas


a = input("Input array a...\n")
print("Sorted by 'insertion' array 'a' is {}.".format(insertion(a)))
