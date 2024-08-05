

import copy

nums = [-1,1,0,-3,3]

def pro(num):
    pro = 1
    for i in num:
        pro *= i

    return pro


nn = pro(nums)
ans = []

for i in nums:
    try:
        val = nn / i
        ans.append(int(val))
    except:
        new = copy.deepcopy(nums)
        new.remove(i)
        ans.append(pro(new))

print(ans)