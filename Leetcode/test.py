nums = [5,20,66,1314]
pos = 0
neg = 0

for i in nums:
    if i < 0:
        neg += 1
    elif i > 0:
        pos += 1
    


print(max(pos,neg))