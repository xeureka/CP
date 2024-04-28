
t = int(input())

lst = []

for i in range(t):
    word = input()
    lst.append(word)


for i in lst:
    if (lst.index(i) +1) %2 !=0:
        print(i)
