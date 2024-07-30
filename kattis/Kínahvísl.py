
# https://open.kattis.com/problems/kinahvisl

word1 = input()
word2 = input()


diff = list(zip(word1,word2))

cout = 1

for i in diff:
    if i[0] != i[1]:
        cout +=1

print(cout)