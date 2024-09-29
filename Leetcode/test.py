nums = [-1,0,1,2,-1,-4]
ans = []

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if (i != j and i != k and j != k) and (nums[i] + nums[j] + nums[k] == 0):
                ans.append([nums[i],nums[j],nums[k]])

print(ans)
