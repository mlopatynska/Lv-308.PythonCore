from random import uniform, randint


def random_list(size):
    rand_list = []
    for i in range(size):
        if randint(0, 1):
            rand_list.append(round(uniform(-size, size), 2))
        else:
            rand_list.append(randint(-size, size))
    return rand_list


a, b, c = random_list(30), random_list(30), random_list(30)
print('a0 - a30 : ', a, '\nb0 - b30 : ', b, '\nc0 - c30 : ', c)


def func(my_list, variable):
    result = 0
    for i in range(30):
        result += my_list[i] * variable ** (30-i)
        #print(my_list[i], result)
    return result


x, y, z = int(input('Please enter variable x: ')), \
          int(input('Please enter variable y: ')), \
          int(input('Please enter variable z: '))

print(f'result: {(func(a, x))**2 - func(b, y) / func(c, x+z) :.5f}')
