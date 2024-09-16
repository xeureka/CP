

def display_student(name,age):
    return f'Name = {name}\nAge = {age}'


print(display_student('Eureka',20))


show_student = display_student


print(show_student('Nan',14))