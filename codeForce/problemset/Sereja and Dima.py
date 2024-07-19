
n = int(input())

ser = []
dim = []
 
lst = list(map(int,input().split()))

for i in range(1,n+1):
    try:
        if i % 2 != 0:
            if lst[0] > lst[-1]:
                ser.append(lst[0])
                lst.remove(lst[0])
            else:
                ser.append(lst[-1])
                lst.remove(lst[0])
        else:
            if lst[0] > lst[-1]:

                ser.append(lst[0])
                lst.remove(lst[0])
            else:
                ser.append(lst[-1])
                lst.remove(lst[-1])
    except:
        break

print(f'{sum(ser)} {sum(dim)}')
