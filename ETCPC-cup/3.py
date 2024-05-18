t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    path = dict()
    for i in range(m):
        u,v = map(int,input().split())
        path[u] = v

    def dfs(node,n):
        if node == n:
            return True
        
        if node in path:
            ans = dfs(path[node], n)
            if ans :
                return True
        return False

    if not dfs(1, n):
        print("NO")

    else:
        print("YES")
