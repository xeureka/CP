
def pali(n):
    n = str(n)
    return n[::-1] == n

num = int(input())

for i in range(num+1,1000):
    if pali(i):
        print(i)
        break