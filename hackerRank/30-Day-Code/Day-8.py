hashh = dict()

n = int(input())

for i in range(n):
    name,phone = map(str,input().split())
    hashh[name] = phone

items = hashh.keys()
for i in range(n):
    val = input()
    if not val in items:
        print('Not Found')
    else:
        print(f'{val}={hashh[val]}')