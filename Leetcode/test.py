from collections import Counter

paragraph ="Bob. hIt, baLl"
banned = ["hit"]

new = ''

# remove all the special chars from the paragraph   -- done
# remove change all the character in to small case
# count the occureenc of each
# print the higest in lower case

new_para = ''



for i in paragraph:
    if i.isalpha() or i == ' ':
        new_para += i.lower()
new_para.strip()

if banned == []:
    lst1 = new_para.split()
    lst1 = dict(Counter(new_para))
    item = [i for i in lst1.items()]
    val = [i for i in lst1.values()]
    fr = max(item)

    for i in item:
        for j in i:
            if j == fr:
                print(i)
else:
    lst = new_para.split()
    # bann = banned[0]

    # for i in lst:
    #     if i == bann:
    #         lst.remove(i)

    for i in lst:
        if i in banned:
            lst.remove(i)


    new = dict(Counter(lst))

    values = [i for i in new.values()]
    items = [i for i in new.items()]

    freq = max(values)

    for i in items:
        for j in i:
            if j == freq:
                print(i[0])
                break

