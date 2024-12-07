nums1 = [1,2,3]
nums2 = [24]


try:
    print(min(set(nums1).intersection(set(nums2))))

except:
    print(-1)