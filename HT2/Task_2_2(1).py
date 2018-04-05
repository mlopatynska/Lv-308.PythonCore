

python_philosophy = """
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
Namespaces are one honking great idea -- let's do more of those!
""".upper()
print python_philosophy
# I'd typing a upper method,in this way did all text with big characters.

better = python_philosophy.count('better'.upper())
never = python_philosophy.count('never'.upper())
is_char = python_philosophy.count('is'.upper())
print """
The \"better\" word are meeting: {} times
\"never\": {} times
\"is\": {} times
""".format(better, never, is_char)
"""
The '.re.findall' method, has find all characters, 
what I've been putting for him. In a case in a first char. is what we look,
and in a second is: where we look. But one thing, it give for us lists with
characters what we are wanting in a string. So another method of len, are
giving for us how many those char. are in list, and this is our final purpose
"""

i_replace = python_philosophy.replace('I', '&')
print i_replace
# No comments =D

