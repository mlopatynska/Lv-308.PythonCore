
def selection_sort(ex_list):
    count = 0
    while count <= len(ex_list) - 1:
        for x in range(count, len(ex_list)):
            if ex_list[x] == min(ex_list[count:]):
                ex_list[count], ex_list[x] = ex_list[x], ex_list[count]
        count += 1
    return ex_list


a = [44, 20, 13, 5, 13, 8, 13, 1, 0, 0, 1, 2, 7, 6, 3, 2]

print selection_sort(a)