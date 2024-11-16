nums = [1, 2, 3, 4, 6]
target = 10

# two pointer method

def two_sum(nums,target):
    left,right = 0,len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return (nums[left] ,nums[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None


print(two_sum(nums,target))