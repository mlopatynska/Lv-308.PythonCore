
def merge_sort(ex_list):
    if len(ex_list) <= 1:
        return ex_list

    mid = len(ex_list)/2
    left = merge_sort(ex_list[:mid])
    right = merge_sort(ex_list[mid:])
    return merge(left, right)


def merge(left, right):
    final = []
    l_count, r_count = 0, 0
    while l_count < len(left) and r_count < len(right):
        if left[l_count] <= right[r_count]:
            final.append(left[l_count])
            l_count += 1
        else:
            final.append(right[r_count])
            r_count += 1
    final.extend(left[l_count:])
    final.extend(right[r_count:])
    return final


a = [44, 20, 13, 5, 13, 8, 13, 1, 0, 0, 1, 2, 7, 6, 3]