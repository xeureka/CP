nums = [-4,-2,1,4,8]



newNums = list(map(lambda x:abs(x),nums))

newNums.sort()


if newNums.count(newNums[0]) > 0:
    print(newNums[0])
else:
    print(max(newNums))