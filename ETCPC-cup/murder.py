from collections import deque
n = int(input())

grid = []
for _ in range(n):
    row = list(map(str, input().split()))
    grid.append(row)

print(grid)

def palindrome(arr):
    l, r = 0, len(arr)-1
    while l <= r:
        if arr[l] != arr[r]:
            return False
        l += 1
        r -= 1
    
    return True

directions = [(1,0), (0,1)]
def bfs(r,c):
    Queue = deque()
    Queue.append((r,c))
    while Queue:
        ro,co = Queue.popleft()
        



