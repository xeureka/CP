# Exercise 6: Display numbers divisible by 5 from a list



lst = list(map(int,input().split()))

def div_5(lst):
    div_by_5 = [i for i in lst if i % 5 == 0]

    for i in div_by_5:
        print(i)


div_5(lst)
