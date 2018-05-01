def quicksort(mas):
    if len(mas) == 1 or len(mas) == 0:
        return(mas[0:len(mas)])
    else:
        m = (len(mas)-1)/2
        key = m
        for i in range(1,m+1):
            if mas[m-i]>mas[m+i]:
                mas[m-i], mas[m+i] = mas[m+i], mas[m-i]
            if mas[key]>=mas[m+i]:
                a = mas.pop(m+i)
                mas.insert(key, a)
                key +=1
            if mas[key]<mas[m-i]:
                a = mas.pop(m - i)
                key-=1
                mas.insert(key+1, a)
        if not (len(mas) % 2) and mas[-1] < mas[key]:
            a = mas.pop(-1)
            mas.insert(0, a)
            key+=1
        new_mas = []
        new_mas.extend(quicksort(mas[0:key]))
        new_mas.append(mas[key])
        new_mas.extend(quicksort(mas[key + 1:]))
        return(new_mas)

A = input("Input array a...\n")
#B = [9,31,3,2,7,1,9,3,0,3,9]
#A = quicksort(B)


print("Sorted by 'quicksort' array 'a' is {}.".format(quicksort(A)))
