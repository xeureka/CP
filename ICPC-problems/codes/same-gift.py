

john = input()
jane = input()

same = 0


for i in john:
    if i in jane:
        same +=1
print(same)