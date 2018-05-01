def binary(mas,el):
    m=len(mas)
    if m == 0 or mas[0]>el or mas[-1]<el:
        key = -1
    elif mas[m/2] == el:
        key = m/2
    elif mas[m/2] > el:
        key = binary(mas[0:m/2], el)
    elif mas[m/2] < el:
        key = binary(mas[m/2:], el)+m/2
    return(key)

def bubble(mas):
    for m in range(len(mas)-1):
        for n in range(len(mas)-1-m):
            if mas[n]> mas[n+1]:
                mas[n], mas[n+1] = mas[n+1], mas[n]
    return mas

A = input("Input ordered array a...\n")
elem = input("Input desired element...\n")


print("Element {} not found.".format(elem) if binary(bubble(A),elem) == -1
      else "{} is {}-th element in ordered array {}.".format(elem, binary(bubble(A),elem)+1, bubble(A)))
