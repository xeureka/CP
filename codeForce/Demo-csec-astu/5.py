n = int(input())

for i in range(n):
    word = input()

    if len(word) >10:
        first = word[0]
        last = word[len(word)-1]

        res = len(word) -2

        print(f'{first}{res}{last}')
    else:
        print(word)