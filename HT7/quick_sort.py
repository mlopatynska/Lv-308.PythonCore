
def quick_sort(ex_list):
    if len(ex_list) <= 1:
        return ex_list
    small, equal, large, = [], [], []
    pivot = ex_list[len(ex_list)/2]

    for x in ex_list:
        if x < pivot:
            small.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            large.append(x)
    return quick_sort(small) + equal + quick_sort(large)


a = [44, 20, 13, 5, 13, 8, 13, 1, 0, 0, 1, 2, 7, 6, 3]

