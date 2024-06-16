
def FizzBuzz(x,y,N):
    
    for i in range(1,N+1):
        if (i % x ==0) and (i % y ==0):
            print('FizzBzz')
        elif (i % x ==0):
            print('Fizz')
        elif (i % y ==0):
            print('Buzz') 
        else:
            print(i)


x,y,N = map(int,input().split())
print(FizzBuzz(x,y,N))

