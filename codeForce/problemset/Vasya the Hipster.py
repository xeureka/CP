# https://codeforces.com/problemset/problem/581/A


lst = list(map(int,input().split()))


print(min(lst), int((max(lst) - min(lst))/2))