# Exercise 2: Append new string in the middle of a given string


first = input("Enter the first string:  ")
second = input("Enter the second string: ")


length = len(first)

middle = 0

if length % 2 ==0:
    middle = length / 2
else:
    middle = length //2

middle = int(middle)
new_str = first[0:middle] + second + first[middle:]

print(new_str)