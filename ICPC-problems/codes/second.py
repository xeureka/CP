

n = int(input())

lst = list(map(int,input().split()))

min1 = min(lst)
max1 = max(lst)


lst = set(lst)

lst = list(lst)

lst.remove(min1)
lst.remove(max1)

max = max(lst)
min = min(lst)

print(f'{min} {max}')