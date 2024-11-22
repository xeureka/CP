
nums = [1,2,3,4,5]

nums2= [6,5,4,2,1]

nums3 = [1,3,2]


def up_mono(nums:list):
    left,right = 0,1
    count = 0

    while right <= len(nums)-1:
        if (nums[left] <= nums[right]):
            left += 1
            right += 1

        else:
            return False
    return True

def down_mono(nums:list):
    left,right = 0,1

    while right <= len(nums) - 1:
        if nums[left] >= nums[right]:
            left += 1
            right += 1
        else:
            return False
    return True

if up_mono(nums3) or down_mono(nums3):
    print(True)
else:
    print(False)