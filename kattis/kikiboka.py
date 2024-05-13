# https://open.kattis.com/contests/mvcb6p/problems/kikiboba

word = input().lower()

numK = word.count('k')
numB = word.count('b')

if numK > numB:
    print('kiki')
elif numB > numK:
    print('boba')
elif numK == numB:
    print('boki')
else:
    print('none')
