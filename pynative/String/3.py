s1 = "America"
s2 = "Japan"


new = s1[0]
new += s2[0]

new += s1[int(len(s1) / 2)]
new += s1[int(len(s2) / 2)]


new += s1[len(s1) - 1]
new += s2[len(s2) - 1]

print(new)