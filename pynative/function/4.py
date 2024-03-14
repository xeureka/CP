'''

Write a program to create a function show_employee() using the following conditions.

    It should accept the employee’s name and salary and display both.
    If the salary is missing in the function call then assign default value 9000 to salary


'''



def show_employee(name,salary=9000):
    return f'Name = {name}\nSalary = {salary} '



print(show_employee("Eureka",8999))
print(show_employee('Bab'))