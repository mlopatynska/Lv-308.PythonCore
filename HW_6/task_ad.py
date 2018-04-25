def rev_str(str):
    s = ''
    for k in range(len(str)-1, -1, -1):
        s =  s + str[k]
    return s
sentence = raw_input("Input your sentence...\n")
print("This sentence is in reverse order: '{}'.".format(rev_str(sentence)))