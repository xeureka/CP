# valid palindrom

# all upper case to lowercase
# remove all non alphanumberic characters


s = " "

def solutioin(s:str):
    word = []

    for i in s:
        if i.isalnum():
            word.append(i.lower())
    
    left,right = 0,len(word) - 1

    while left <= right:
        if word[left] != word[right]:
            return False
        else:
            left += 1
            right -= 1

    return True
              
print(solutioin(s))