
# https://codeforces.com/problemset/problem/141/A

from collections import Counter

guest = input()
host = input()

pile = input()

name = guest + host

count_name = Counter(name)
count_pile = Counter(pile)

if count_pile == count_name:
    print('YES')
else:
    print('NO')