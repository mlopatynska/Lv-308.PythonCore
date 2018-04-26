def reverse_word(word):
    new_word = ''
    for letters in range(1, len(word)+1):
        new_word += word[-letters]
    return new_word


print(reverse_word('Hello how are You?'))

