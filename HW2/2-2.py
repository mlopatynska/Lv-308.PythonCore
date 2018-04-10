#1 write Python philosophy as a string
zen_of_python = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!\n"""

print (
    "Python phylosophy in uppercase:\n{0}\n"
    "'&' instead of 'i':\n{1}\n"
    "Words 'better', 'never' "
    "and 'is' repeats here {2} {3}"
    " and {4} times.\n".format(
                        zen_of_python.upper(),
                        zen_of_python.replace('i','&'),
                        zen_of_python.count('better'),
                        zen_of_python.count('never'),
                        zen_of_python.count('is')))

#2 4-digit number
x = raw_input("Enter 4-digit number: \n")
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])
mult_digits = a*b*c*d 
 
#multiplication of digits of number x
print "\n multiplication of digits of number: {}*{}*{}*{} = {}".format(a, b, c, d, mult_digits)

#sorting digits of number x
print "\n sorted:", sorted(x)

#reverse digits of number x
print "\n reversed:", list(reversed(x))


#3 Change values between 2 variables without using 3rd value
a = 1
b = 2
print "\n changing values a=>b, b=>a:\n", a, b
a,b  = b,a
print a,b