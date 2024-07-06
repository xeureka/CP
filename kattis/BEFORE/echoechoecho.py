# https://open.kattis.com/contests/mvcb6p/problems/oddecho

n = int(input())

lst = []

for i in range(n):
    word = input()
    lst.append(word)

for char in lst:
    if (lst.index(char) == 0):
        
        print(char)
    elif (lst.index(char) % 2 ==0):
       
        print(char)
     