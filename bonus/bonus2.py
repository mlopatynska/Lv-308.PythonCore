
var1 = raw_input("Enter anything: ")

var2 = len(var1)/3
# Have dividing length of string on 3 pieces

t_list = [var1[:var2], var1[var2+1:var2*2], var1[var2*2+1:-1]]
# Was creating a list, which include 3 variables from one typed of string.
print t_list
