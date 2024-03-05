name = input('Enter your name:  ')


name = list(name)
lst = []
str1 = ''

for i in name:
    if type(i) == int:
        print(i)
    else:
        print('no number yet')        
    
