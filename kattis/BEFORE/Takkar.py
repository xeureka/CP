# https://open.kattis.com/problems/takkar

a = int(input())
b = int(input())

if a > b:
    print('MAGA!')
elif b > a:
    print('FAKE NEWS!')
else:
    print('WORLD WAR 3!')
