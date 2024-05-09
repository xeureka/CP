# https://codeforces.com/problemset/problem/49/A

word = input().lower()

vowel = [a,e,i,o,u,y]

last = word[len(word) - 1]

if last in vowel:
  print("YES")
else:
  print("NO")
