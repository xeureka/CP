word = "abcd"
ch = "z"

num = word.index(ch)

w = word[:num+1]
other = word[num+1:]

ans = w[::-1] + other

print(ans)