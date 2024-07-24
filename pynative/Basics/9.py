# Exercise 9: Check Palindrome Number

num = input()

def pali(num):
    if num == num[::-1]:
        return True
    return False


print(pali(num))