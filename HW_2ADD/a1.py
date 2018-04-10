x = [1, 2, 4]
y = x[:]
a, b, c = x

#I way. Variables A, B, C are going to have as value as list x
A = B = C = list(x)
print("List 'x' is {},\n"
      "list 'y' is {}; \n"
      "but id(x)={}, id(y)={}".format(x,
                                      y,
                                      id(x),
                                      id(y)))
print("3 numbers of the list are...{}, {}, {}".format(a, b, c))

print("I way. 3 lists are...{}, {}, {}".format(A, B, C))

#II way. I understood the the task not completely. Maybe you mean this?

from math import floor

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
xlen_3 = int(floor(len(X)/3))

A_3 = X[:xlen_3]
B_3 = X[xlen_3:2*xlen_3]
C_3 = X[2*xlen_3:]
print("II way. The initial list was {}. It is divided by about a third: {}, {}, {}.".format(X, A_3, B_3, C_3))