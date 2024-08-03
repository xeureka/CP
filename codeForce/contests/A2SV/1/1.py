# https://codeforces.com/gym/540458/problem/0


n = []

a = 0
b = 0


for i in range(int(input())):
    word = input()

    n.append(word)

    ans = n[0]

    if word == ans:
        a +=1
    else:
        b += 1


if a > b:
    print(ans)

else:
    for i in n:
        if i != ans:
            print(i)
            break






