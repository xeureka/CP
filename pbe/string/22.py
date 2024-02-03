
'''
022

Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.
'''

firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')

fullName = firstName.title() + ' '+ lastName.title()
print(fullName)