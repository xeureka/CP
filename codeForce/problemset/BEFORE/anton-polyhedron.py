# https://codeforces.com/problemset/problem/785/A



n = int(input())

lst = []
for i in range(n):
    word = input()
    lst.append(word)

value= {'Tetrahedron':4,
        'Cube':6,
        'Octahedron':8,
        'Dodecahedron':12,
        'Icosahedron':20}

cout = 0

for i in lst:
    cout += value[i]

print(cout)