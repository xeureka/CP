num1,num2,num3 = map(int,input().split())
order = input().lower()

lst = [num1,num2,num3]
lst.sort()
a = lst[0]
b = lst[1]
c = lst[2]

if order == 'abc':
    print(a, b, c)
elif order== 'acb':
    print(a, c, b)
elif order == 'bac':
    print(b, a, c)
elif order == 'bca':
    print(b, c, a)
elif order == 'cab':
    print(c, a, b)
elif order == 'cba':
    print(c, b, a)
else:
    print()


