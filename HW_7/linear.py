def linear(mas,el):
    key = -1
    for i in range(len(mas)):
        if mas[i] == el:
            key = i
    return(key)

A = input("Input array a...\n")
elem = input("Input desired element...\n")
print("Element {} not found.".format(elem) if linear(A,elem) == -1
      else "{} is {}-th element in given array.".format(elem,linear(A,elem)+1))
