# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

ran = [[1,50]]
left = 1
right = 50

new = []
check = list(range(left,right+1))



for i in ran:
    for j in i:
        new.append(j)

new.sort()

cout = 0

if (left == right) and (right in new):
    print(True)
elif (len(new) == 2) and ([left,right] == new):
    print(True)
else:
    for i in check:
        if i in new:
            cout += 1
        
if cout == len(check):
    print(True)
else:
    print(False)