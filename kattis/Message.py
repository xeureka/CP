# https://open.kattis.com/problems/meddelande


n,m = map(int,input().split())

lst = []


for i in range(n):
    new = input()

    lst.append(new)

new = []

for item in lst:
    for j in item:
        if j != '.':
            print(j,end='')
            




