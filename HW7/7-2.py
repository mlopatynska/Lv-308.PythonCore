# 7-2
def selection(a):
    """function for sorting arrays by selection method"""

    for i in range(len(a)-1):
        min_el = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_el]:
                min_el = j
        a[i], a[min_el] = a[min_el], a[i]
    return a


my_list = [16, 12, 8, 5, 3, 15, 14, 7]
print(f"Unsorted list:", my_list)
print(f"\nSorted by selection method:", selection(my_list))

