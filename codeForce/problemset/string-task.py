# https://codeforces.com/contest/118/problem/A

word = input()
vowels = [ "a", "o", "y", "e", "u", "i"]

word = list(word)
new = []

for i in word:
    i = i.lower()
    if not i in vowels:
        new.append('.')
        new.append(i)

for i in new:
    print(i,end='')