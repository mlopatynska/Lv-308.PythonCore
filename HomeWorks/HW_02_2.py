# encoding=utf8
import sys, re
reload(sys)
sys.setdefaultencoding('utf8')


philosophy = """
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
There should be one—and preferably only one—obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let's do more of those!
"""
list = re.split(" ", philosophy.lower().replace("." or "," or "\n", ""))
def word_couter(word, text):
    cout = 0
    for i in text:
        if word == i:
            cout += 1
    return cout
def num_couter(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum

print(word_couter("better", list))
print(word_couter("never", list))
print(word_couter("is", list))
print(philosophy.upper())
print(philosophy.replace("i", "&"))

numbers = str(raw_input())
print(num_couter(numbers))
print(numbers[::-1])

a, b = 0, 1
print(a, b)
a, b = b, a
print(a, b)