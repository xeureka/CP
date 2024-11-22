# at least 3 characters
# only alpha numberic
# at leat one vlowel
# at least one consonant

word = "a3$e"

def valid(word:str):
    cCount,vCount = 0,0

    vowel = set(['a', 'e', 'i', 'o', 'u'])


    if len(word) < 3:
        return False
    
    for char in word:
        if not char.isalnum():
            return False
        
        if not char.isdigit():
            if char.lower() in vowel:
                vCount += 1
            
            else:
                cCount += 1
        
        
        

    if vCount > 0 and cCount > 0:
        return True
    return False



    

    
    
print(valid(word))
                



    


    