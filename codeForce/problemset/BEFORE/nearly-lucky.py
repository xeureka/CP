# https://codeforces.com/problemset/problem/110/A


num = input()
cout = 0
for i in num:
    if i == '4' or i =='7':
        cout +=1

if cout == 7 or cout ==4:
    print('YES')
else:
    print('NO')