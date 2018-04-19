word = input('Enter a word: ')
myDict = {}
for count in range(len(word)):
    times = word.count(word[count])
    myDict[word[count]] = times
print(f'Yuo can find such amount of letters in "{word}": ', myDict)
