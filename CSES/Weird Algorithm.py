# https://cses.fi/problemset/task/1068

def main(n):
    
    while n != 1:
        print(n,end=' ')
        if n % 2 != 0:
            n = n * 3 + 1
        else:
            n //=2
    print(1)
        
    
n = int(input())
main(n)

