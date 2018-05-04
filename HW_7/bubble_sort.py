def bubble_sort(x):
    for i in range(len(x) - 1):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
    return bubble_sort(x)

n = input("Enter massif n: ")

print("Sorted massif 'n' is {}.".format(mysort(n)))