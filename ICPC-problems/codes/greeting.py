# twice as many ee's

gre = input()

new = ''

e = gre.count('e')

new = 'e' * (e*2)
print(gre[0] + new + gre[len(gre) -1])