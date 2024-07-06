# https://codeforces.com/contest/1829/problem/A

for i in range(int(input())):
    word = input()

    target = 'codeforces'

    new = list(zip(word,target))
    
    count = 10
    
    if target == word:
        print(0)
    else:
        for item in new:
            if item[0] == item[1]:
                count -=1
        print(count)

        