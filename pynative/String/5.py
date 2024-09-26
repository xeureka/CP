str1 = "P@#yn26at^&i5ve"

char = 0
dig = 0
sym = 0

for i in str1:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        dig += 1
    else:
        sym += 1

print(f'Chars = {char}')
print(f'Digits = {dig}')
print(f'Symbol = {sym}')