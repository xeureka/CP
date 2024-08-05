nums = ["777","7","77","77"]
target = "7777"


count = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        if (i != j) and (nums[i] + nums[j] == target):
            count += 1

print(count)