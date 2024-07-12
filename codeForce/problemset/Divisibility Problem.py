# https://codeforces.com/problemset/problem/1328/A


def func(a,b):
        cout = 0

        while True:
            if a % b ==0:
                return cout
            else:
                a +=1
                cout +=1

for i in range(int(input())):
    a,b = map(int,input().split())
    print(func(a,b))

    

    


    