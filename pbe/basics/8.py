'''
008
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay.

'''

totalBill = int(input('ENter the totalprice: '))

person = int(input('Enter how many peoples are there in the dinner: '))

indivisualPice = totalBill / person

print(f'Each person must pay {indivisualPice}')
