

def bubble_sort(any_list):
    count = 1
    while count < len(any_list):
        for n in range(len(any_list)-1):
            if any_list[n] > any_list[n+1]:
                any_list[n+1], any_list[n] = any_list[n], any_list[n+1]
        count += 1
    return any_list


a = [44, 20, 13, 5, 13, 8, 13, 1, 0, 0, 1, 2, 7, 6, 3, 2]
print bubble_sort(a)
