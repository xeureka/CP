
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true


def average(array):
    # your code goes here
    array = set(array)

    length = len(array)

    sum = 0

    for i in array:
        sum += i


    average = sum / length
    return average
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)