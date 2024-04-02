

# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

m,a = int(input()), set(map(int,input().split()))
n,b = int(input()), set(map(int,input().split()))


print(*sorted(a ^ b),sep='\n')