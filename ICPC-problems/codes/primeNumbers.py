
def prime(num):
    prime = True

    for i in range(2,num+1):
        if num % i ==0:
            prime = False
            break
        
    else:
        prime = True

    return prime

t = int(input())

for i in range(t):
    n = int(input())

    no = 0

    for i in range(2,n+1):
        if prime(n):
            no +=1

    print(n)

    