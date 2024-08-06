# for i in range(int(input())):
#     n = input()

#     sum = 0

#     for i in n:
#         sum += int(i)
#     print(sum)

# problem 2 starts here

for i in range(int(input())):
    lst = list(map(int,input().split()))
    su = lst[:2]
    sl = lst[2:]

    comb = list(zip(su,sl))

    rev = su[::-1]

    comb2 = list(zip(rev,sl))

    count = 0

    answer = 0

    for i in comb:
        if i[0] > i[1]:
            count += 1

    if count == 2:
        answer += 1

    count2 = 0

    for i in comb2:
        if i[0] > i[1]:
            count2 += 1

    if count2 ==2:
        answer += 1

    print(answer*2)

     

    


        


    

    
        
    
