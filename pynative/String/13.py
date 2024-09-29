str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
ans = []

for i in str_list:
    if (i != "") and (i != None):
        ans.append(i)

print(ans)