#  https://codeforces.com/problemset/problem/703/A

arr = []

for i in range(int(input())):
    game = tuple(map(int,input().split()))
    arr.append(game)

m,c,tie = 0,0,0

for i in arr:
    if i[0] > i[1]:
        m +=1
    elif i[1] > i[0]:
        c +=1
    else:
        tie +=1

if m > c:
    print('Mishka')
elif m == c:
    print('Friendship is magic!^^')
else:
    print('Chris')