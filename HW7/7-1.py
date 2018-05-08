#7-1
def bubble(a):
    """function for sorting arrays by bubble_sort method"""

    last_el = len(a)-1
    for i in range(last_el):
        for x in range(last_el - i):
            if a[x] > a[x+1]:
                a[x+1], a[x] = a[x], a[x+1]
    return a


my_list = [16, 12, 8, 5, 3, 15, 14, 7]
print(f"Unsorted list:", my_list)
print(f"\nSorted by bubble's method:", bubble(my_list))
bubble(my_list)
