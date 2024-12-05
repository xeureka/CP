

n,target = map(int,input().split())

arr = list(map(int,input().split()))

# brute force solution


def solution(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] + arr[j] == target:
                return [i+1,j+1]