# https://codeforces.com/problemset/problem/1472/B

for i in range(int(input())):
    n =int(input())
    lst = list(map(int,input().split()))

    one = lst.count(1)
    two = lst.count(2)

    if ((one +  2 * two) % 2 !=0):
        print('NO')
    else:
        sum = (one + 2 * two)/2
        if (sum % 2 ==0 or (sum % 2 ==1 and one != 0)):
            print('YES')
        else:
            print('NO')



     

    