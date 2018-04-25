
def perestanovka(txt, other_txt):
    answer = ''
    if sorted(txt) == sorted(other_txt):
        answer = 'the {} word is equal to {}.'.format(txt, other_txt)
    else:
        for count in range(0,6):
            txt_count = raw_input('Enter one more word: ')
            if sorted(txt_count) == sorted(other_txt):
                answer = 'the {} word is equal to {}.'.format(txt_count, other_txt)
                break
            else:
                answer = False
    return answer


print perestanovka('rever', 'reverse')