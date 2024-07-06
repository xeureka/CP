# https://codeforces.com/problemset/problem/1722/B

n = int(input())


for i in range(n):
    t = int(input())

    word1 = input().lower()
    word2 = input().lower()

    word1 = list(word1)
    word2 = list(word2)

    combined = list(zip(word1,word2))

    nonI = [('r','b'),('b','r'),('r','g'),('g','r')]
    cout = 0

    for item in combined:
        if item in nonI:
            cout += 1

    if cout >= 1:
        print('NO')
    else:
        print('YES')

