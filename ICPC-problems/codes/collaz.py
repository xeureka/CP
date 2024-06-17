n = int(input())

arr = []

val = n
arr.append(val)

while val >= 1:
    
    if val % 2 == 0:
        val /= 2
        arr.append(val)
        
    else:
        val = 2*val + 1
        arr.append(val)
        

print(arr)