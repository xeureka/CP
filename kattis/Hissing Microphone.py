# https://open.kattis.com/problems/hissingmicrophone


word = input()


s = word.index('s')

if word[s + 1] == 's':
    print('hiss')
else:
    print('no hiss')