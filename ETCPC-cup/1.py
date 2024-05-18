n = int(input())
for i in range(n):
    s,r = map(str,input().split())
    cout = 0

    for i in range(len(s)):
        if s[i] != r[i]:
            cout += 1
    
    print(cout)