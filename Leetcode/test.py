
name = 'three two one'
lst = name.split()

lst.reverse()

ans = ''

for i in lst:
    ans += ' '
    ans += i

print(ans.strip())