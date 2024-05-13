# https://codeforces.com/problemset/problem/49/A

word = input().lower()


vowel = ['a','e','i','o','u','y']

new = word[:(len(word) -1)]
x = new.strip()


if x[len(x) - 1] in vowel:
    print('YES')
else:
    print('NO')

