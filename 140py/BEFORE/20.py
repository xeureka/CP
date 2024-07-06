# Write a Python Program to Find Armstrong Number in an Interval.

num1 = input()
num2 = input()

length = len(num)

cout = 0

for digit in num:
    digit = int(digit)
    cout += digit **length

num = int(num)
if cout == num:
    print(f"{num} is armstrong number")
else:
    print(f'{num} is not armstrong number')