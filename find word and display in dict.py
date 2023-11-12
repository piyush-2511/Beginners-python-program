def findword(sen,words):
    d={}
    words = sen.split()
    for i,w in enumerate(words):
        if w==words:
            d[i]=words
    return d

sen = input('enter the sentence : ')
words = input('enter the word : ')
d = findword(sen,words)
print(d)
