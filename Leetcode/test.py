word1 = "ace"
word2 = "bd"

comb = ''

cout = 0

if len(word1) > len(word2):
    cout = len(word1)
    
    for i in range(cout):
        try:
            comb += word1[i] + word2[i]
        except:
            comb += word1[i]
    

elif len(word1) < len(word2):
    cout = len(word2)

    for i in range(cout):
        try:
            comb += word1[i] + word2[i]
        except:
            comb += word2[i]
else:
    cout = len(word1)

    for i in range(cout):
        comb += word1[i] + word2[i]

print(comb)

# ans = ''
# lst = tuple(zip(word1,word2))

# for i in lst:
#     for j in i:
#         ans += j



# if len(word1) > len(word2):
#     new = word1[len(word2)-1:]
#     ans += new

# else:
#     new = word2[len(word2) -2 :]
#     ans += new

# print(ans)
