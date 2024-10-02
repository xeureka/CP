
# https://codeforces.com/contest/1850/problem/C


for i in range(int(input())):

    grid = []

    for i in range(8):
        lst = list(map(str,input().split()))
        grid.append(lst)
    
    ans = [k for items in grid for item in items for k in item if k.isalpha()]
    
    final = ''
    for i in ans:
        final += i
    
    print(final)