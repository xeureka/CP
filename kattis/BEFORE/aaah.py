john = input()
doc = input()


count1 = 0
for i in john:
    count1 +=1
    
count2 = 0

for i in doc:
    count2 +=1
    
if count1 < count2:
    print('no')
else:
    print('go')