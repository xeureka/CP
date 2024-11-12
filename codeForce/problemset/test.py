#  0 to 127 inclusive
# a and b
# abs(a-b)

#  either 5 or 7 semitones


for i in range(int(input())):
    t = int(input())
    a,b = map(int,input().split())

    semitone = abs(a - b)
    if semitone == 5 or semitone == 7:
        print('YES')
    else:
        print('NO')