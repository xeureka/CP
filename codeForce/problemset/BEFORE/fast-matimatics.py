# https://codeforces.com/problemset/problem/61/A

num1 = input()
num2 = input()

ans = list(zip(num1,num2))

sum = ''

for i in ans:
    if i[0] == i[1]:
        sum +='0'
    else:
        sum +='1'

print(sum)

    