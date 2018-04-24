# hash
word = raw_input("Enter any word: ")
word_set = set(word)
hash = {i:word.count(i)for i in  word_set }
print hash
