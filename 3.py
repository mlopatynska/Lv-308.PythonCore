a = raw_input("Enter some sentence\n")
list = a.split()
list.sort(key=len, reverse=True)
print ",".join(list)


