nums = [-10,8,6,7,-2,-3]

def solut(nums:list) -> int:
    if max(nums) and -max(nums) in nums:
        return max(nums)
    
    num = []
    
    for i in nums:
        if -i in nums:
            num.append(i)
    
    if len(num) > 0:
        return max(num)
    
    return -1




print(solut(nums))