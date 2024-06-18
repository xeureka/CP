# in revierse order
# lower becomes upper and upper becomes lower


word = input()

new = ''

for item in word:
    if item.isupper():
        item = item.upper()
        new += item

    else:
        item = item.lower()
        new += item

print(new[::-1])