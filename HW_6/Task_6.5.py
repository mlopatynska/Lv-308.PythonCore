def mysort(x):
    for i in range(len(x) - 1):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
    return mysort(x)

n = input("Enter massif n: ")
m = input("Enter massif m: ")

print("Sorted massif 'n' is {}.".format(mysort(n)))
print("Sorted massif 'm' is {}.".format(mysort(m)))