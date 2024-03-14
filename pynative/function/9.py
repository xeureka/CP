# Exercise 9: Find the largest item from a given list


def larg(*lst):
    
    lst = list(lst)


    large = max(lst)

    return large



print(larg(1,2,3,4,5))