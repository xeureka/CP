str1 = "/*Jon is @developer & musician"

ans = ''

for i in str1:
    if i.isalnum() or i == ' ':
        ans += i

print(ans)