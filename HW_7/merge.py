def merge(A, B):
    C=[]
    while len(A)*len(B)>0:
        if A[0] < B[0]:
            c = A.pop(0)
        else:
            c = B.pop(0)
        C.append(c)
    if len(A)>0:
        C.extend(A)
    else:
        C.extend(B)
    return C

a = input("Input array a...\n")

A = []
for m in range(len(a)):
    F = []
    F.append(a[m])
    A.append(F)

m = len(A)
while m > 1:
    D=[]
    for n in range(0, m/2):
        D.append(merge(A[2*n],A[2*n+1]))
    if m%2 and len(A[-1]) != 0:
        D.append(A[-1])
    m = len(D)
    A=D

print("Sorted by 'merge' array 'a' is {}.".format(A[0]))
