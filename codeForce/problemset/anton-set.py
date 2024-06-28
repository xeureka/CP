# https://codeforces.com/problemset/problem/443/A


word = input()
new = []

for i in word:
    if i not in ['{','}',' ',','] and i not in new:
        new.append(i)

print(len(new))
