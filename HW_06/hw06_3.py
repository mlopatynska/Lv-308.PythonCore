def my_dict(word):
    myDict = {}
    for i in range(len(word)):
        f = word.count(word[i])
        myDict[word[i]] = f
    return myDict


def Perestanovka(x, y):
    count = 0
    for i in my_dict(y):
        for a in my_dict(x):
            if my_dict(y)[i] <= my_dict(x)[a] and i == a:
                count += 1
    if count == len(my_dict(y)):
        return True


words = [input("Enter a word: ") for i in range(5)]

for i in words[1:]:
    if Perestanovka(words[0], i):
        print(f"You can create '{i}' from '{words[0]}' letters")
    else:
        print(f"You can not create '{i}' from '{words[0]}' ")

