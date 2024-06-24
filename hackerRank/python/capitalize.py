


# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true


word = input()

def solve(s):
    num = ['1','2','3','4','5','6','7','8','9','0']
    
    name = word.split(' ')
    ans = ''
    
    for item in name:
        if item[0] in num:
            ans += item
            ans += ' '
        else:
            ans += item.title()
            ans += ' '   
            
             
    return ans

print(solve(word))
