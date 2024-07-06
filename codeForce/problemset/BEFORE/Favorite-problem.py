import string

lst = list(string.ascii_lowercase)

for i in range(int(input())):
    num = int(input())
    word = input()

    new = []

    for i in word:
        new.append(lst.index(i))


    print(max(new) + 1)
    
    