

n,k = input().split()
n = int(n)
k = int(k)

score = list(map(int,input().split()))


count = 0

for i in score:
    if i > k:
        count +=1

    
print(count)