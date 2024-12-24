

# input = two sorted arrays of integers
# output = the merged array


nums1 = [1,3,15]
nums2 = [1,3,9,15,20]

def solu(nums1:list,nums2:list):
    left,right = 0,0
    result = []

    while left < len(nums1) and right < len(nums2):
        if nums1[left] <= nums2[right]:
            result.append(nums1[left])
            left += 1
        else:
            result.append(nums2[right])
            right += 1
    
    while left < len(nums1):
        result.append(nums1[left])
        left += 1
    
    while right < len(nums2):
        result.append(nums2[right])
        right += 1
    

    return result
    



print(solu(nums1,nums2))