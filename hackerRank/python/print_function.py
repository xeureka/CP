# https://www.hackerrank.com/challenges/python-print/

if __name__ == '__main__':
    n = int(input())
    
    def num_lst(n):
        for i in range(1,n+1):
            print(i,end='')
            
    num_lst(n)

