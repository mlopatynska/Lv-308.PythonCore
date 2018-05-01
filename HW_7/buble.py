def bubble(mas):
    for m in range(len(mas)-1):
        for n in range(len(mas)-1-m):
            if mas[n]> mas[n+1]:
                mas[n], mas[n+1] = mas[n+1], mas[n]
    return mas


def bubble_r(mas):
    m_new=[]
    if len(mas) == 1:
        m_new.append(mas[0])
    else:
        for n in range(len(mas)-2,-1,-1):
            if mas[n]> mas[n+1]:
                mas[n], mas[n+1] = mas[n+1], mas[n]
        m = mas.pop(0)
        m_new.append(m)
        m_new.extend(bubble_r(mas))
    return m_new


a = input("Input array a...\n")

print("Sorted by 'bubble' array 'a' is {}.".format(bubble(a)))

print("Sorted by 'recursive bubble' array 'a' is {}.".format(bubble_r(a)))

