word = input()


new = ''


for i in word:
    if i.isupper():
        new +=i

print(new)