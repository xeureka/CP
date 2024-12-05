arr = [10,2,5,3]


def sol(arr:int) -> bool:
    left,right = 0,len(arr) - 1

    while left <= right:
        if (arr[left] == 2*arr[right]) or (arr[right] == 2* arr[left]):
            return True
        
        left += 1
        right -= 1
    
    return False


print(sol(arr))