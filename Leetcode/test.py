nums = [1,2,3,4]


def solution(nums:list) -> list:
    total_sum = 1

    for i in nums:
        total_sum *= i

    result = []

    for i in nums:
        result.append(int(total_sum / i))
    
    return result

print(solution(nums))
        