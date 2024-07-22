# https://codeforces.com/gym/537460/problem/E

answer = 'ABCDEFGHIJKLMNOPQRZTUVWXYS'




word = input()

count_q = word.count('?')

word = set(word)

if len(word) <26:
    print(-1)

else:
    if len(word) + count_q == 26:
        print(answer)
    else:
        print(-1)