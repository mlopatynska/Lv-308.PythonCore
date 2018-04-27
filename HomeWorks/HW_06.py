def compare_words(first_word, *words):
    for i in words:
        if sorted(i) == sorted(first_word):
            print(i)



def bubble_sort(list, reverse = False):
    '''
    :param list: Any list of integers
    :param reverse: reverse = True if you want to get reverse list. Default to False
    :return: return new and sorted list
    '''
    ranger = len(list)
    while ranger > 0:
        for i in range(ranger-1):
            if list[i] > list[i + 1]:
                change = list[i]
                list[i] = list[i + 1]
                list[i + 1] = change
        ranger -= 1
    if not reverse:
        return list
    else:
        return list[::-1]




massive = [1, 2, 4, 121, 22, 23239, 2823, 9384, 11]
print(len(bubble_sort(massive)))
