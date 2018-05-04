


def appender():
    #For ex1
    import random
    list_var = []
    for i in range(30):
        list_var.append(random.randint(-100, 100))
    return list_var

#ex1
a, b, c, x, y, z = appender(), appender(), appender(), int(input()), int(input()), int(input())
def math_ref(supernum, secondnum):
    result = 0
    for i in range(30):
        result += supernum[i] * secondnum **(30-i)
    return result

ex_1_res = math_ref(a, x)**2 -math_ref(b, y) / math_ref(c, x + z)
print(ex_1_res)
#ex2
def loop_factorial(x):
    if x is 0:
        return 1
    else:
        return x * loop_factorial(x-1)

#ex3
def Perestanovka(first_word, *words):
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





