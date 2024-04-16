

# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true


num_eng,val_eng = int(input()),set(map(int,input().split()))
num_fre,val_fre = int(input()),set(map(int,input().split()))


result = val_eng.union(val_fre)
print(len(result))