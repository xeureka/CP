
nums = list(map(int,input().split()))

order = input()
order = list(order)


ans = list(zip(order,nums))

ans.sort()

for item in ans:
    print(item[1],end=' ')
