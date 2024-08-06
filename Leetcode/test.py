nums = [8,1,2,2,3]
ans = []
count = 0

for i in nums:
    
    count = 0

    for j in nums:
        if i > j:
            count += 1
    ans.append(count)

        

print(ans)

