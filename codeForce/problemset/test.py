
def find_missing_integer(integers):
    
    integer_set = set(integers)
    
    for x in range(2, 21):  
        n = 10 ** x
        
        
        if n not in integer_set:
            if int(str(n)[:-x]) in integer_set:
                return n
    
    return None






for i in range(int(input())):
    word = int(input())
    print(find_missing_integer(word))

    