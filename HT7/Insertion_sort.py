
def insertion_sort(ex_list):
    for x in range(1, len(ex_list)):
        var = ex_list[x]
        prevar = x - 1
        while prevar >= 0:
            if var < ex_list[prevar]:
                ex_list[prevar + 1], ex_list[prevar] = ex_list[prevar], var
            prevar -= 1
    return ex_list


a = [44, 20, 13, 5, 13, 8, 13, 1, 0, 0, 1, 2, 7, 6, 3, 2]

print insertion_sort(a)