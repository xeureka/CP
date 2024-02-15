# Making calculator by using the object orinted programming concept

class Calculator:

    def __init__(self,x,y):
        self.x = x
        self.y = y


    def addition(self):
        return self.x + self.y
    
    def subtraction(self):
        return f"{self.x} - {self.y}"
    
    def mult(self):
        return f"{self.x} * {self.y}"
    

    def division(self):
        return f"{self.x} / {self.y}"
    

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
            except ValueError as e:
                print(e)
                print("Please enter the input in a correct format")
            else:
                result = Calculator(num1,num2)
                print(result.addition())
