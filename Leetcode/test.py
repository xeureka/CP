

s = "leetcode"

# convert the string to list
# declare list containing vowels
# declare right and left pointer
# is both left and right are in vowel swap their value
#  is left not inc left
# else inc right

def solu(s:str) -> str:
    s = list(s)

    left,right = 0,len(s) -1

    vow = ['a', 'e', 'i', 'o', 'u']

    while left <= right:
        if (s[left].lower() in vow) and (s[right].lower() in vow):
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        
        elif not s[left].lower() in vow:
            left += 1
        
        else:
            right -= 1
    
    return ''.join(s)
  


print(solu(s))