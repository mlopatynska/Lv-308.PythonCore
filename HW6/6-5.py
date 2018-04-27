def bubble(mass):
    """function for sorting arrays by bubble_sort method"""

    last_el = len(mass)-1
    for i in range(0, last_el):
        for x in range(0, last_el - i):
            if mass[x] < mass[x+1]:
                mass[x+1], mass[x] = mass[x], mass[x+1]

    return mass


list_1 = [25, 12, 78, 98, 56, 99]
list_2 = [12, 4, 45, 40, 5, 68, 13]

print(f'Unsorted list_1: {list_1}\nUnsorted list_2: {list_2}\n')
print(f'Sorted list_1: {bubble(list_1)}\nSorted list_2: {bubble(list_2)}')