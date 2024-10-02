word = str(input('Write a word: '))
w = len(word)
print(w)

for i in range(0, w - 1, 2):
    print(word[i])