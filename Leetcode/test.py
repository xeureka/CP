nums = [3,2,2,3]
val = 3

def sol(nums,val):
    
    l = 0

    for i in range(len(nums)):

        if nums[i] != val:
            nums[l],nums[i] = nums[i],nums[l]
            l += 1
    

    return i