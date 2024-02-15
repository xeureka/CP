# Making calculator by using the object orinted programming concept

class Calculator:

    def __init__(self,x):
        self.x = x

    def __add__(self,number2):
        return self.x + number2.x
    
    def __sub__(self,number2):
        return self.x - number2.x
    
    def __mul__(self,number2):
        return self.x * number2.x
    
    def __div__(self,number2):
        return self.x / number2.x



print('''
            |                               |
            |   WELCOME TO BAB calculator   |
            |                               |
''')

while True:
    print('             MENUES:  ') 
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Quit')


    try:
        user = int(input("Enter you choice:   "))
    except ValueError as e:
        print(e)
        print('Please enter a correct input.')
    else:
        if user == 1:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the other number:  "))

                number1 = Calculator(num1)
                number2 = Calculator(num2)
            except ValueError as e:
                print(e)
                print("Please enter the input in a correct format")
            else:
                print(number1 + number2)
        
        elif user == 2:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the other number:  "))

                number1 = Calculator(num1)
                number2 = Calculator(num2)
            except ValueError as e:
                print(e)
                print("Please enter the input in a correct format")
            else:
                print(number1 - number2)
           
        elif user == 3:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the other number:  "))

                number1 = Calculator(num1)
                number2 = Calculator(num2)
            except ValueError as e:
                print(e)
                print("Please enter the input in a correct format")
            else:
                print(number1 * number2)

        elif user ==4:
            try: 
                num1 = int(input("ENter the first number:  "))
                num2 = int(input("Enter the other number:  "))
                
                number1 = Calculator(num1)
                number2 = Calculator(num2)

            except ZeroDivisionError as e:
                print(e)
                print('We cant divide a number by zero so please try to finx your input')
            except ValueError as e:
                print(e)
                print("Pleae enter your input correctly")

        elif user == 5:
            try:
                break
            except ValueError as e:
                print(e)
                print("Pleae enter your value correctly")
        else:

            print("Please enter the correct choice")