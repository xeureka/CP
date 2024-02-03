'''
032

Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.

'''
from math import pi as pi

radius = int(input('Enter the radius of the cylinder: '))
height = int(input('ENter the height of the cylinder: '))


area = pi * (radius **2)

volume = height * area

volume = round(volume,3)

print(f'The volume of the cylinder is {volume}')

