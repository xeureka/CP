n = int(input())

d = {}

for i in range(n):
    name, phone = map(str, input().split())
    d[name] = int(phone)
    
while True:
    try:
        NAME = input()
        if NAME in d:
            print(f'{NAME}={d[NAME]}')
        else:
            print('Not found')
    except EOFError:
        break
    