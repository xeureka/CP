# Exercise 4: Remove first n characters from a string

def remove_chars(word,index):
    new_str = word[index:]
    return new_str



word = input()
num = int(input())

print(remove_chars(word,num))