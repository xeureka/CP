def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i

    return fact


t = int(input())

for i in range(t):
    n = int(input())
    print(fact(n))