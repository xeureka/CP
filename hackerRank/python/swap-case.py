# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true


def swap_case(s):
    



    new = ''

    for i in s:
        if i.islower():
            new +=i.upper()
        elif i.isupper():
            new +=i.lower()
        else:
            new +=i
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)