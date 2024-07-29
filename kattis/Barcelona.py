# https://open.kattis.com/problems/barcelona

n,k = map(int,input().split())

lst = tuple(map(int,input().split()))


place = lst.index(k)

if place == 0:
    print('fyrst')
elif place == 1:
    print('naestfyrst')
else:
    print(f'{place + 1} fyrst')