# print all prime numbers under 1,000,000

def is_prime(num):
    prime = True

    for i in range(2,num):
        if (num % i) ==0:
            prime = False
            break

    else:
        return prime
    
for i in range(1,100):
    if is_prime(i):
        print(i)
    