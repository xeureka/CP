# https://www.codewars.com/kata/558fc85d8fd1938afb000014

def lowest_sum(arr):
    arr.sort()

    return arr[0] + arr[1]



arr = [19,5,2,77]

print(lowest_sum(arr))