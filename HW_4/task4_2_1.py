my_str = raw_input("Input your string...\n")
my_set = set(my_str)
hesh = []
for let in my_set:
    hesh.append(str(let) + " : " + str(my_str.count(let)))
print(hesh)
