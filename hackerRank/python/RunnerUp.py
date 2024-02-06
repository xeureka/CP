
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
    arr = set(arr)
    
    arr = list(arr)
    arr.sort(reverse=True)
    
    print(arr[1])