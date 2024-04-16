# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true


i,m = int(input()),set(map(int,input().split()))
j,n = int(input()), set(map(int,input().split()))


print(*sorted(m | n),sep='\n')