def my_min(mas):
    min_mas = mas[0]
    position = 0
    for m in range(len(mas)):
        if min_mas > mas[m]:
            min_mas = mas[m]
            position = m
    return position

def selection(mas):
    for m in range(len(mas)-1):
        mnew = my_min(mas[m:len(mas)])+m
        mas[m], mas[mnew] = mas[mnew], mas[m]
    return mas


a = input("Input array a...\n")
print("Sorted by 'selection' array 'a' is {}.".format(selection(a)))
