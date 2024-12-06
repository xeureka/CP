s = 'egg'
t = 'add'

def solution(s,t):
    if len(s) != len(t):
        return False
    sStack,tStack = [],[]

    for i in range(len(s)):
        sStack.append(s.index(s[i]))
        tStack.append(t.index(t[i]))
    
    return sStack == tStack

print(solution(s,t))