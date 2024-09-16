s1 = "Ault"
s2 = "Kelly"


new = s1[0:int(len(s1) / 2)]
new += s2

new += s1[int(len(s1) / 2):]

print(new)