# https://cses.fi/problemset/task/1083

def missingNumber(nums):
    n = len(nums)

    s = set(nums)

    for num in range(n+1):
        if num not in s:
            return num
        

n = int(input())
nums = list(map(int,input().split()))

missingNumber(nums)