from collections import deque

# creating zip of closing -> opening char  == completed

# iterate over s and append opening to the stack
# if i is closing and if stack[-1] and i in zip stack.pop()
# else return False
# if not stack return True else return False

s = "([])"


def solution(s:str) ->bool:
    stack = deque()

    
    combined = {')':'(',
                '}':'{',
                ']':'['}
    for char in s:
        if not char in combined:
            stack.append(char)
        
        elif (char in combined) and (combined[char] == stack[-1]):
            stack.pop()
        else:
            return False
    
    return not stack


print(solution(s))
        
        