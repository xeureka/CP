
# https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

from math import pow as pow


a = int(input())
b = int(input())
c = int(input())


print(int(pow(a,b)))
print(int(pow(a,b) % c))