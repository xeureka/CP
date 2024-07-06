

# https://codeforces.com/problemset/problem/734/A


n = int(input())
score = input()

score = list(score)

if score.count('A') > score.count('D'):
    print('Anton')
elif score.count('D') > score.count('A'):
    print('Danik')
else:
    print('Friendship')