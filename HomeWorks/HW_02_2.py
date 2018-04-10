# encoding=utf8

philosophy = u"""The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!"""







# Here we will consider the number of different words: better, never, is
t = 'times'
print("better",philosophy.count("better"), t)

print("never",philosophy.count("never"),t)
print('is', philosophy.count("is"),t)
# Here we write a philosophy in the large print
print(philosophy.upper())
# Here we write a replacing 'i' letter with &
print(philosophy.replace("i", "&"))

numbers = str(input("Print four numbers: "))
# Dividing numbers into variables
one, two, three, four = int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])
print(one * two * three * four)
# reversing string with numbers
print(numbers[::-1])
# sorting numbers
print(sorted(numbers))
# We change the values of two variables without using the third variable
a, b = 0, 1
print(a, b)
a, b = b, a
print(a, b)