import string

alphabets = list(string.ascii_lowercase)

def get_data():
    word = input('Please enter the word to be decoded: ')

    num = int(input('Pleaeenter the sift number: '))

    if num > 26 or num ==0:
        while num > 26 or num ==0:
            num = int(input('NUmber out of range please enter a number between 1 - 26: '))

    data = (word,num)

    return data