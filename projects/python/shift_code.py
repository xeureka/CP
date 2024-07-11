import string

alphabet = list(string.ascii_lowercase)


def get_data():
    word = input('Enter a word: ').lower()
    num = int(input('Enter a number between 1 - 26 '))

    if num > 26 and num ==0:
        while num > 26 and num ==0:
            num = int(input('Number out of range enter a number betweeen 1 - 26'))

    data = (word,num)

    return data
def make_code(word,num):
    new_word = ""

    for x in word:
        y = alphabet.index(x)
        y -= num

        if y > 26:
            y += 27
        
        char = alphabet[y]
        new_word += char

    return new_word

def decode(word,num):
    new_word = ''

    for x in word:
        y = alphabet.index(x)
        y -= num

        if y < 0:
            y += 27
        
        char = alphabet[y]

        new_word += char

        return new_word

def main():
    again = True

    while again == True:
        print('1. Make a code')
        print('2.Decode a code')
        print('3. Quit')

        usr = int(input('\tEnter Your Choice Here:  '))

        (word,num) = get_data()
        if usr == 1:
            
            print(make_code(word,num))
        elif usr == 2:
            
            print(decode(word,num))
        else:
            again = False

    
main()
        
