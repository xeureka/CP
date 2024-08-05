nums = [1,2,3,4]


ans = []

sum = nums[0]

for i in range(len(nums)):
    if i == 0:
        ans.append(sum)
    else:
        sum += nums[i]
        ans.append(sum)

print(ans)
    