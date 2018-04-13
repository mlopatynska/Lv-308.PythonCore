#Copy x to y  so that id(x) != id(y), but x == y.
x = [ 1, 2 ]
y = x
print (('x = {}\ny = {}\n    id(x )= {}\n\
    id(y )={}\n').format(x, y, id(x ), id(y )))


#Transfer list value  that contain 3 elements to 3 variables
x = [ 1, 2, 3 ]
y  = x
a, b, c  = y
print ('\n a = {}\n b = {}\n c ={} '.format(a, b, c ) )

#Transfer list value of any lenght to 3 variables
a = b = c = x
print ('\n a = {}\n b = {}\n c ={} '.format(a, b, c ) )



