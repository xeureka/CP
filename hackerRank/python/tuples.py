#https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true



if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))


    integer_list = tuple(integer_list)
   
    print(hash(integer_list))