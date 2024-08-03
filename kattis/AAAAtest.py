# this is test site
# /https://open.kattis.com/problems/skammstofun?editresubmit=13973998

n = int(input())

word = input()


new = ''

for i in word:
    if i.isupper():
        new += i

print(new)