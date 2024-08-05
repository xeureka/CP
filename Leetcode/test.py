nums = [10,4,8,3]


def leftSum(num):
    ans = []

    for i in num:
        try:
            i = num.index(i) + 1
            val = num[i:]
            ans.append(sum(val))
        except:
            ans.append(0)

    return ans


def rightSum(num):
    pass


    


