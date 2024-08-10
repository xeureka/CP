from collections import Counter

s = 'tree'
new = Counter(s)

ans = ''

for i,j in new.items():
    ans += i*j

print(ans)