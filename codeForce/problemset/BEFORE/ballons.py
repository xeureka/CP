
for i in range(int(input())):
    n = int(input())
    word = input().lower()

    new = []

    ballon = 0

    for i in word:
        if not i in new:
            new.append(i)
            ballon +=2
        elif i in new:
            ballon +=1
    
    print(ballon)
