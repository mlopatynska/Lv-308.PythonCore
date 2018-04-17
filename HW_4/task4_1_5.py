my_str, first_sym = raw_input("Input your text...\n"), raw_input("Input first symbols...\n")
my_list = my_str.split()
count = 0
for sym in my_list:
    if (str(sym))[0:len(first_sym)] == first_sym:
        print(sym)
        count += 1
print("{} words start with characters '{}'.".format(count, first_sym))