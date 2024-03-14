# Exercise 7: Assign a different name to function and call it through the new name


def stud(name,age):
    return f'{name}   {age}'




student = stud


print(student('Eureka',12))