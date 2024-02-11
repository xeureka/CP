try:
    num1 = int(input('Enter number1: '))
    num2 = int(input('Enter number 2:  '))

    div = num1 / num2

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print('ERROR ')
except:
    print('Unexpeted error')

else:
    print(div)
