
n = int(input())

def sum(n):
    sum = 0

    for i in range(1,n+1):
        sum += n

    return sum

print(sum(n))