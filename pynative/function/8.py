# Exercise 8: Generate a Python list of all the even numbers between 4 to 30


# method 1 = iterative approach
def even_nums():
    lst = []
    for num in range(4,31):
        if num % 2 ==0:
            lst.append(num)



    return lst



print(even_nums())



# method 2 = list comphrension

def evens():
    lst = [num for num in range(4,31) if num % 2 ==0]

    return lst


print(evens())