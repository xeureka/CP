nums = [9]

fake = ''

for i in nums:
    i = str(i)
    fake += i

new  = int(fake) + 1


ans = [int (i) for i in str(new)]
print(ans)