

txt = 'The most kind of people characters is our freedom, in kingdom we will rise, kit'
count = 0
finish = False

while not finish:
    print txt
    f_symbol = raw_input('Please enter a symbols, what you wont to find: ')
    for search in range(0, len(txt) + 1):
        if f_symbol not in txt:
            print 'Sorry, but your symbols are not exist in a text.'
            finish = True
            break
        elif search == txt.find(f_symbol, count)\
                and txt[txt.find(f_symbol, count) - 1] == " ":
            symbol_start = txt[txt.find(f_symbol, count):].split()
            count = txt.find(f_symbol, count) + 1
            print symbol_start[0]
        elif search == txt.find(f_symbol, count)\
                and txt[txt.find(f_symbol, count) - 1] != " ":
            count = txt.find(f_symbol, count) + 1
            continue
        elif txt.find(f_symbol, count) == -1:
            finish = True



