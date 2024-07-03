
# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    new = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new.append([name,score])
        
    score = []

    for item in new:
        score.append(item[1])

    mini = min(score)
    

    for i in score:
        if i == mini:
            score.remove(i)

    second_min = min(score)

    sN = []

    for i in new:
        if i[1] ==second_min:
            sN.append(i[0])

    sN.sort()
    for i in sN:
        print(i)
        
        
        
        
        
