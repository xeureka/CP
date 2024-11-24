nums = [1,1,0,1,1,1]

def solution(nums:list):
    current_count=max_count = 0

    for value in nums:
        if value == 1:
            current_count += 1

        else:

            max_count = max(max_count,current_count)
            current_count = 0
    
    return max(current_count,max_count)


            

print(solution(nums))
            
