

lst = list(map(int,input().split()))

def same(lst):
    if lst[0] == lst[len(lst) - 1]:
        return True
    return False

print(same(lst))