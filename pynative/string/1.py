# Exercise 1A: Create a string made of the first, middle and last character
# https://pynative.com/python-string-exercise/#h-exercise-1a-create-a-string-made-of-the-first-middle-and-last-character
str1 = input("Enter the string: ")

leng = len(str1)
midd = 0

if leng % 2 ==0:
    midd = leng /2
else:
    midd = leng //2


new_string = str1[0] + str1[midd] + str1[leng-1]

print(new_string)