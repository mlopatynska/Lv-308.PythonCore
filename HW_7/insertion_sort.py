def Insertion_Sort(x):
    for j in range(1,len(x)):
        key = x[j] 
        i = j-1 
        while (i > -1) and key < x[i]: 
            x[i+1]=x[i] 
            i=i-1 
        x[i+1] = key
    return x
x = [5,2,4,6,1,3]

print(Insertion_Sort(x))