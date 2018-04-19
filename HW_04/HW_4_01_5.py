count = 0
text = input('Enter your text: ')
search = input('What to find: ')
yourText = list(text.split(' '))
print('Result: ')
for i in yourText:
    i = str(i)
    if i[:len(search)] == search:
        count += 1
        print(count, i)
if not count:
    print('I found nothing')
