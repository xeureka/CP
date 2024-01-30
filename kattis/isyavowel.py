vowel = ['a','e','i','o','u']

val = input().lower()

count = 0
y = 0


for i in val:
    if i in vowel:
        count +=1
        

for i in val:
    if i == 'y':
        y +=1
        
sum = count + y

print(f'{count} {sum}')
        