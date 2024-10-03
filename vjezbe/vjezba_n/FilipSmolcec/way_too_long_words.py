n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)
for word in words:
    if len(word) <= 10:
        print(word)
    else:
        s = word[0] + str(len(word)-2) + word[len(word)-1]
        print(s)