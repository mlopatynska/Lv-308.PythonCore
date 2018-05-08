#7-3
def insertion(a):
    """function for sorting arrays by insertion sort method"""

    for i in range(len(a)):
        for x in range(i-1, -1, -1):
            if a[x] > a[x+1]:
                a[x+1], a[x] = a[x], a[x+1]
    return a


my_list = [25, 12, 8, 5, 3, 15, 14, 7]
print(f"Unsorted list:{my_list},\n"
      f"Sorted by insertion's sort method:",
      insertion(my_list))

