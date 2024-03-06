# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true


if __name__ == '__main__':
    lst = []
    min_s = 100
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < min_s:
            min_s = score
        lst.append([name,score])

    
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][1] 


    