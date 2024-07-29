# https://open.kattis.com/problems/bijele


correct = [1,1,2,2,2,8]

lst = list(map(int,input().split()))

zipped = list(zip(correct,lst))

new = []

for item in zipped:
    val = item[0] - item[1]
    new.append(val)


for i in new:
    print(i,end=' ')