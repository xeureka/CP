# https://codeforces.com/contest/1996/problem/A

for i in range(int(input())):
    n = int(input())

    if n <= 2:
        print(1)
    else:
        animal = 0

        if n % 4 ==0:
            animal += n // 4
        else:
            animal += (n//4) + 1

        print(animal)