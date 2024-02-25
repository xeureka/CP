# Exercise 1B: Create a string made of the middle three characters


str1 = input("Enter the string: ")

length = len(str1)
middle = 0

if length % 2 ==0:
    middle = length / 2
else:
    middle = length //2

new_str = str1[middle-1] + str1[middle] + str1[middle+1]

print(new_str)
