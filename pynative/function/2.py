

# Write a program to create function func1() to accept a variable length of arguments and print their value.


def func1(*vals):
    for i in vals:
        print(i)



func1(1,2,3,4,5,'Eureka','Nan','Bab')