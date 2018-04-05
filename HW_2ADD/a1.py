x = [1, 2, 4]
y = x[:]
a, b, c = x
A = B = C = list(x)
print("List 'x' is {},\n"
      "list 'y' is {}; \n"
      "but id(x)={}, id(y)={}".format(x,
                                      y,
                                      id(x),
                                      id(y)))
print("3 numbers of the list are...{}, {}, {}".format(a, b, c))

print("3 lists are...{}, {}, {}".format(A, B, C))
