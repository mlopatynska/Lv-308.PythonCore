

def bubble_sort(any_list):
    count = 0
    while count < len(any_list):
        for n in range(len(any_list)-1):
            if any_list[n] > any_list[n+1]:
                any_list[n+1], any_list[n] = any_list[n], any_list[n+1]
                count += 1
    return any_list


a = [1, 2, 5, 8, 7, 6, 3]
print bubble_sort(a)
