# https://codeforces.com/problemset/problem/266/A


n = int(input())

stones = input()

cout = 0

for i in range(n):
    try:
        if stones[i] == stones[i+1]:
            cout +=1
    except:
        break

print(cout)