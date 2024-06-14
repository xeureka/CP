# change the given number to binary

for i in range(int(input())):
    x = int(input())
    binary = bin(x)
    print(binary[2:])