def perestanovka(x, y):
    list_x = sorted(list(x))
    list_y = sorted(list(y))
    if list_x == list_y:
        return True
    else:
        return False

words = [raw_input("input word...\n") for k in range(5)]
for k in range(1,5):
    if perestanovka(words[k],words[0]):
        print("The word '{}' may be obtained from word '{}'.".format(words[k], words[0]))

