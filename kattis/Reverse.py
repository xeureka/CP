# https://open.kattis.com/problems/ofugsnuid

lst = []

for i in range(int(input())):
    num = int(input())
    lst.append(num)


lst.reverse()

for i in lst:
    print(i)