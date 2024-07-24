# Exercise 3: Print characters from a string that are present at an even index number

word = input()


for i in range(len(word)):
    if i % 2 ==0 or i ==0:
        print(word[i])