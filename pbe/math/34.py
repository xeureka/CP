'''
034


Display the following message:
If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else

'''

print('1) square\n2)Triangle')

value = input('ENter a number: ')


if value ==1:
    width = int(input('width '))
    height = int(input('height '))

    area = width * height

    print(f'The area of the square is {area}')
elif value == 2:
    width = int(input('width '))
    height = int(input('height '))

    area = (height * width) * (1/2)

    print(f'The area of the traingale is {area}')
else:
    print('You entered a wrong input')
