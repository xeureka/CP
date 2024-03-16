
# https://codeforces.com/gym/511717/problem/F


t = int(input())

for i in range(t):
    ticket = input()

    dig = [int(digit) for digit in ticket]


    first = sum(dig[:3])
    sec = sum(dig[3:])



    if first == sec:
        print("YES")
    else:
        print("NO")