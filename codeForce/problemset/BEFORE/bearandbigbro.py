x,y = map(int,input().split())


lstX = []
lstY= []

for i in range(20):
    lstX.append(x)
    x = 3 * x

for i in range(20):
    lstY.append(y)
    y = 2 * y


new  = list(zip(lstX,lstY))

for item in new:
    if item[0] > item[1]:
        print(new.index(item))
        break
