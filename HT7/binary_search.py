
def binary_search(ex_list, find):
    if len(ex_list) == 0 or (len(ex_list) == 1 and ex_list[0] != find):
        return False

    mid = len(ex_list)/2
    if find == ex_list[mid]:
        return True
    elif find < ex_list[mid]:
        return binary_search(ex_list[:mid], find)
    elif find > ex_list[mid]:
        return binary_search(ex_list[mid:], find)


a = [0, 0, 1, 1, 2, 3, 5, 6, 7, 8, 13, 13, 13, 20, 44]
