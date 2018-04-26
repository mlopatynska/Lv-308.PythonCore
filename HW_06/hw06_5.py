from random import randint


def my_sort(x):
    c = 0
    while c < len(x):
        for i in range(len(x)-1):
            if x[i] < x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
        c += 1
    return x


size = int(input("Enter the size of the list: "))
my_list = [randint(-size, size) for i in range(size)]
print(f'Random list:        {my_list}\n' 
      f'Sorted with bubble: {my_sort(my_list)}')
