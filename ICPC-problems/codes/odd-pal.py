# odd palindrom = odd length + palindrom

word = input()

def pali(word):
    return word[::-1] == word

def odd(length):
    return length % 2 !=0


if pali(word) and odd(len(word)):
    print('Odd.')
else:
    print('Or not.')