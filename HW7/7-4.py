# 7-4
def merge_sort(a):
    """function for sorting arrays by merge sort method"""

    if len(a) < 2:
        return a
    mid = int(len(a)/2)
    left_part = merge_sort(a[:mid])
    right_part = merge_sort(a[mid:])
    return merge(left_part, right_part)


def merge(left_part, right_part):
    """merge arrays"""


    sorted_a = []
    i = j = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            sorted_a.append(left_part[i])
            i += 1
        else:
            sorted_a.append(right_part[j])
            j += 1

    sorted_a.extend(left_part[i])
    sorted_a.extend(right_part[j])
    return sorted_a


my_list = [2, 6, 12, 1, 9, 5]
sorted_a = merge_sort(my_list)
print(sorted_a)
