s = "Test1ng-Leet=code-Q!"

def solu(s:str):
    s = list(s)

    left,right = 0,len(s) -1

    while left <= right:
         
        if s[left].isalpha() and s[right].isalpha():
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        
        elif s[left].isalpha() == False:
            left += 1
        
        else:
            right -= 1
    
    return ''.join(s)

        


print(solu(s))


