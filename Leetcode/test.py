nums = [-4,-2,1,4,8]

ans = nums[0]

for x in nums:
    if abs(x) < abs(ans):
        ans = x

if ans < 0 and abs(ans) in nums:
    print(abs(ans))
else:
    print(ans)