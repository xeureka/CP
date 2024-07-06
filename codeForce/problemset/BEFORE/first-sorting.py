# https://codeforces.com/problemset/problem/1971/A

n = int(input())

for i in range(n):
	x,y = map(int,input().split())
	if x>y:
		print(f'{y} {x}')
	else:
		print(f'{x} {y}')
